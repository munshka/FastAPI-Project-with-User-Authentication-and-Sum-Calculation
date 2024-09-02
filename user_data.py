import pandas as pd
from passlib.context import CryptContext

def get_password_hash(password):
    return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(password)

def auth():
    df = pd.read_excel('users_api.xlsx')

    # Define a function to convert each row into the desired dictionary format
    def row_to_dict(row):
        return {
            'username': row['USERNAME'],
            'full_name': row['FULL_NAME'],
            'email': row['USER_ID'],
            'hashed_password': get_password_hash(row['PASSWORD']),  # Hash the password
            'disabled': not bool(row['IS_ACTIVE'])  # Convert IS_ACTIVE to boolean and invert
        }

    # Convert each row of the DataFrame into a dictionary and store in a list
    data = [row_to_dict(row) for index, row in df.iterrows()]

    # Convert list of dictionaries into a nested dictionary with 'username' as key
    db = {row['username']: row for row in data}
    return db