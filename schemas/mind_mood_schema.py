from pydantic import BaseModel
from typing import List

class MindMoodData(BaseModel):
    name: str
    intensity: str
    resolved: bool
    end_date: str
    entry_date: str
    entry_note: str

class MindMoodDataRequest(BaseModel):
    version: str
    data: List[MindMoodData]
