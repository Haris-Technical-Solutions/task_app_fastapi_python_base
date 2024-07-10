from pydantic import BaseModel, Field
from typing import Optional


class UpdateForm(BaseModel):
    content:str
    # parent_id :Optional[int] = None
    # project_id :int
    # assignee_id :int
    # parent_id :Optional[int]