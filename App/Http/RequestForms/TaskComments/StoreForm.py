from pydantic import BaseModel, Field
from typing import Optional


class StoreForm(BaseModel):
    content :str
    parent_id :Optional[int] = None
