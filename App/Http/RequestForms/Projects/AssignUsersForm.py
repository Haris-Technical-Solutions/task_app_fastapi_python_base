from pydantic import BaseModel, Field
from typing import Optional

class AssignUsersForm(BaseModel):
    users: list[int]