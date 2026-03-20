from pydantic import BaseModel
from typing import List

class ActivityData(BaseModel):
    name: str
    duration: int
    distance: int
    calories: float
    entry_date: str
    entry_note: str

class ActivityDataRequest(BaseModel):
    version: str
    data: List[ActivityData]
