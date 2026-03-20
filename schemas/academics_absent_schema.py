from pydantic import BaseModel
from typing import List

class AcademicsAbsentData(BaseModel):
    reason: str
    absent_date: str
    entry_date: str
    entry_note: str

class AcademicsAbsentDataRequest(BaseModel):
    version: str
    data: List[AcademicsAbsentData]
