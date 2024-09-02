from fastapi import Depends, FastAPI,HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
import config
import user_data
from pydantic import BaseModel
from typing import Optional
import auth

class SumResult(BaseModel):
    result: int

class Token(BaseModel):
    access_token:str
    token_type: str

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

app= FastAPI()

@app.post("/token", response_model=Token)
async def login_for_access_token(from_data:OAuth2PasswordRequestForm=Depends()):
    user = auth.authenticate_user(user_data.auth(),from_data.username, from_data.password)
    if not user:
         raise  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token= auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/users/me/", response_model=User)
async def read_users_me(current_user:User =Depends(auth.get_current_active_user)):
    #time.sleep(120)
    return current_user


@app.post("/sum/" ,response_model=SumResult)
async def sum_numbers(data: dict = Body(...), current_user:User =Depends(auth.get_current_active_user)):
    
    num1 = data.get("num1")
    num2 = data.get("num2")
    return {"result": num1 + num2}