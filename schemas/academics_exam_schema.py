from pydantic import BaseModel
from typing import List

class AcademicsExamData(BaseModel):
    subject: str
    exam_type: str
    exam_date: str
    duration: int
    entry_date: str
    entry_note: str

class AcademicsExamDataRequest(BaseModel):
    version: str
    data: List[AcademicsExamData]
