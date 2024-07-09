from pydantic import BaseModel, Field
from typing import Optional
from App.Http.Models.User import UserRoles


class UserStoreForm(BaseModel):
    name: str
    second_name: Optional[str] = None
    email: str
    role: UserRoles = Field(..., description="Role of the user. Possible values: 'admin', 'user'")
    password: str
    c_password: str 