
from fastapi import Depends, HTTPException, status, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Annotated
from datetime import datetime, timedelta, timezone
import jwt
from passlib.context import CryptContext
from jwt.exceptions import InvalidTokenError

from App.v1.Providers.database import db
from App.v1.Models.User import User


from App.v1.RequestForms.Auth import LoginForm , RegisterForm


SECRET_KEY = "f6790033fe3181b9e6388b963a0802041629b09179ff380a6c792f4d6713a7c1"
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


class AuthServiceProvider:
    def __init__(self):
        self.db = db()
    class Token(BaseModel):
        access_token: str
        token_type: str

    class TokenData(BaseModel):
        email: str | None = None

    class UserInDB(RegisterForm.RegisterForm):
        hashed_password: str

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

   
    def get_user(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

   
    def authenticate_user(self, email: str, password: str):
        user = self.get_user(email)
        if not user:
            return False
        if not self.verify_password(password, user.password):
            return False
        return user
    
    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    async def login_for_access_token(self, form_data: Annotated[LoginForm.LoginForm, Depends()]) -> Token:
        # return form_data
        user = self.authenticate_user(form_data.email, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        return self.Token(access_token=access_token, token_type="bearer")

    async def get_current_user(self, token: Annotated[str, Depends(oauth2_scheme)]):
        # return token
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            email: str = payload.get("sub")
            if email is None:
                raise credentials_exception
            token_data = self.TokenData(email=email)
        except InvalidTokenError:
            raise credentials_exception
        user = self.get_user(email=token_data.email)
        if user is None:
            raise credentials_exception
        return user

    async def get_current_active_user(self, current_user: Annotated[RegisterForm.RegisterForm, Depends(get_current_user)]):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user

    async def read_users_me(self, current_user: Annotated[RegisterForm.RegisterForm, Depends(get_current_active_user)]):
        return current_user

    async def read_own_items(self, current_user: Annotated[RegisterForm.RegisterForm, Depends(get_current_active_user)]):
        return [{"item_id": "Foo", "owner": current_user.email}]
