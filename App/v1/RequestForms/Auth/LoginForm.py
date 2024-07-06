from pydantic import BaseModel
from typing import Optional


class LoginForm(BaseModel):
    email: str
    password: str
    remember_me: Optional[bool] = False
    