from pydantic import BaseModel
from typing import Optional


class RegisterForm(BaseModel):
    name: Optional[str] = None
    second_name: Optional[str] = None
    email: str
    password: str
    c_password: str 
    # status: str
    # # deleted_at: Optional[datetime] = None