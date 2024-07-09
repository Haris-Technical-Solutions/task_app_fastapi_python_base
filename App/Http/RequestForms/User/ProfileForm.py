from pydantic import BaseModel
from typing import Optional


class ProfileForm(BaseModel):
    name: Optional[str] = None
    second_name: Optional[str] = None
    email: Optional[str] = None
    old_password: Optional[str] = None
    password: Optional[str] = None
    c_password: Optional[str] = None