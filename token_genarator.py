from api_client import FastAPIClient

# Example usage
username = "aaa"
password = "aaa111"

base_url = "http://127.0.0.2:7000"  # Update with your FastAPI server URL
api_client = FastAPIClient(base_url)

try:
    access_token = api_client.authenticate_user(username, password)
    print("Authentication successful.")
    print("Access token:", access_token)

except ValueError as e:
    print("Error:", e)
