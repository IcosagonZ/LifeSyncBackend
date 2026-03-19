# FastAPI backend for LifeSyncAI
# Run using fastapi dev

from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "status": "OK",
        "version": "0.1.0"
    }

@app.post("/client/version")
async def read_client_version(request: Request):
    data = await request.json();
    print("Client>Data {}".format(data))
    return {
        "status": "OK",
        "version": "0.1.0"
    }

class AcademicsAbsentData(BaseModel):
    reason: str
    absent_date: str
    entry_date: str
    entry_note: str

class AcademicsAbsentDataRequest(BaseModel):
    version: str
    data: List[AcademicsAbsentData]

class AcademicsAssignmentData(BaseModel):
    subject: str
    type: str
    topic: str
    submitted: int
    due_date: str
    submission_date: str
    entry_date: str
    entry_note: str

class AcademicsAssignmentRequest(BaseModel):
    version: str
    data: List[AcademicsAssignmentData]

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

class BodyMeasurementData(BaseModel):
    measurement_type: str
    value: float
    unit: str
    entry_date: str
    entry_note: str

class BodyMeasurementDataRequest(BaseModel):
    version: str
    data: List[BodyMeasurementData]

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

class NoteData(BaseModel):
    title: str
    content: str
    tags: str
    entry_date: str

class NoteDataRequest(BaseModel):
    version: str
    data: List[NoteData]

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

class TimeData(BaseModel):
    event: str
    duration: int
    entry_date: str
    entry_note: str

class TimeDataRequest(BaseModel):
    version: str
    data: List[TimeData]

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

class VitalsData(BaseModel):
  type: str
  value: str
  unit: str
  entry_date: str
  entry_note: str

class VitalsDataRequest(BaseModel):
    version: str
    data: List[VitalsData]

class NutritionData(BaseModel):
    name: str
    form: str
    type: str
    qty: float
    calories: float
    mass: float
    carbs: float
    protein: float
    fats: float
    entry_date: str
    entry_note: str

class NutritionDataRequest(BaseModel):
    version: str
    data: List[NutritionData]

@app.post("/recommendations/nutrition")
async def read_data_vitals(payload: NutritionDataRequest):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    recommendation = [
    ]

    insight = [
    ]

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "nutrition",
        "score": 67,
        "recommendation": recommendation,
        "insight": insight,
    }
