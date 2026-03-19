from pydantic import BaseModel
from typing import List

class WorkoutData(BaseModel):
    name: str
    type: str
    duration: int
    calories: float
    reps: int
    weight: float
    entry_date: str
    entry_note: str

class WorkoutDataRequest(BaseModel):
    version: str
    data: List[WorkoutData]
