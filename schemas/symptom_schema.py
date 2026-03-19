from pydantic import BaseModel
from typing import List

class SymptomData(BaseModel):
    name: str
    intensity: int
    resolved: int
    end_date: str
    entry_date: str
    entry_note: str

class SymptomDataRequest(BaseModel):
    version: str
    data: List[SymptomData]
