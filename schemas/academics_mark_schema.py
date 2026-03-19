from pydantic import BaseModel
from typing import List

class AcademicsMarkData(BaseModel):
    subject: str
    type: str
    marks: float
    marks_total: float
    entry_date: str
    entry_note: str

class AcademicsMarkDataRequest(BaseModel):
    version: str
    data: List[AcademicsMarkData]
