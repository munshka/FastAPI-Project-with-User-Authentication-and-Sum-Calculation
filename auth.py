#Command -> uvicorn main:app --reload

from fastapi import Depends, FastAPI,HTTPException, status, Body
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Optional
from datetime import datetime,timedelta
from jose import JWTError,jwt
from passlib.context import CryptContext
import pandas as pd
import config
import user_data


class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str


def verify_password(plain_password,hashed_password):
    return CryptContext(schemes=["bcrypt"], deprecated="auto").verify(plain_password,hashed_password)


def get_user(db,username:str):
    if username in db:
        user_data = db[username]
        return UserInDB(**user_data)

def authenticate_user(db, username:str, password:str):
    user= get_user(db,username)
    if not user:
        return False
    if not verify_password(password,user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, config.SECRECT_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(token, config.SECRECT_KEY, algorithms=[config.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception

    user = get_user(user_data.auth(), username=token_data.username)
    if user is None:
        raise credential_exception

    return user

async def get_current_active_user(current_user: UserInDB= Depends(get_current_user)):
    if current_user.disabled:
        raise  HTTPException(status_code=400,detail="Inactive user")
    return current_user






   


