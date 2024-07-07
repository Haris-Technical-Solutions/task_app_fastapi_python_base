from pydantic import BaseModel
from typing import Optional
# from App.Http.RequestForms.Auth import Token


class Token(BaseModel):
    token: str 
    