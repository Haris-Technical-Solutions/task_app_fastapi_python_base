from pydantic import BaseModel, Field
from typing import Optional


class UpdateForm(BaseModel):
    title: str
    description :Optional[str] = None
    status :str
    # project_id :int
    # assignee_id :int
    # parent_id :Optional[int]