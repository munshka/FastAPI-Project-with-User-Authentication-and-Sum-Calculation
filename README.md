# FastAPI-Project-with-User-Authentication-and-Sum-Calculation


This project is a FastAPI application that includes user authentication, user profile retrieval, and a simple API for summing two numbers.

Features
User Authentication: 
Secure login using OAuth2 with password hashing and JWT token-based authentication.

User Profile Retrieval: 
Retrieve the current authenticated user's profile.

Sum Calculation: 
An API endpoint that calculates the sum of two numbers.

Requirements
Python 3.7+
FastAPI
Pydantic
Dependencies are not listed in requirements.txt

Installation
Clone the repository:

git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate


Install the dependencies:
Copy code
pip install -r requirements.txt
Configure environment variables or settings:


Update the config.py file with your settings, such as the ACCESS_TOKEN_EXPIRE_MINUTES.

Running the Application

Start the FastAPI server:
uvicorn main:app --reload
The application will be available at http://127.0.0.1:8000.

API Endpoints
1. Obtain Token
URL: /token
Method: POST
Description: Authenticate the user and receive an access token.

Payload:
{
  "username": "your_username",
  "password": "your_password"
}
Response:
{
  "access_token": "your_access_token",
  "token_type": "bearer"
}

2. Get User Profile
URL: /users/me/
Method: POST
Description: Retrieve the profile of the currently authenticated user.
Headers:
Authorization: Bearer <access_token>
Response:
{
  "username": "your_username",
  "email": "your_email",
  "full_name": "Your Full Name",
  "disabled": false
}
