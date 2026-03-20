from pydantic import BaseModel
from typing import List

class NoteData(BaseModel):
    title: str
    content: str
    tags: str
    entry_date: str

class NoteDataRequest(BaseModel):
    version: str
    data: List[NoteData]
