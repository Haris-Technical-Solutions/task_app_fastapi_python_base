from pydantic import BaseModel, Field
from typing import Optional


class UpdateForm(BaseModel):
    name: str