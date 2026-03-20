from pydantic import BaseModel
from typing import List

class AcademicsAssignmentData(BaseModel):
    subject: str
    type: str
    topic: str
    submitted: int
    due_date: str
    submission_date: str
    entry_date: str
    entry_note: str

class AcademicsAssignmentDataRequest(BaseModel):
    version: str
    data: List[AcademicsAssignmentData]
