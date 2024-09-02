import requests

class FastAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def authenticate_user(self, username: str, password: str) -> str:
        token_url = f"{self.base_url}/token"
        data = {"username": username, "password": password}
        response = requests.post(token_url, data=data)
        if response.status_code == 200:
            return response.json()["access_token"]
        else:
            raise ValueError("Authentication failed")

    def get_current_user(self, access_token: str) -> dict:
        user_url = f"{self.base_url}/users/me/"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(user_url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError("Failed to get user data")

    def get_current_user_items(self, access_token: str) -> list:
        items_url = f"{self.base_url}/users/me/items"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(items_url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError("Failed to get user items")
        
  
    def sum_numbers(self, num1: int, num2: int, access_token: str) -> dict:
        sum_url = f"{self.base_url}/sum/"
        data = {"num1": num1, "num2": num2}
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.post(sum_url, json=data, headers=headers)
        if response.status_code == 200:
            return response.json()["result"]
        else:
            raise ValueError("Failed to calculate sum")

    



