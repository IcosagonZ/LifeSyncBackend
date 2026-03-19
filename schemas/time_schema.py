from pydantic import BaseModel
from typing import List

class TimeData(BaseModel):
    event: str
    duration: int
    entry_date: str
    entry_note: str

class TimeDataRequest(BaseModel):
    version: str
    data: List[TimeData]
