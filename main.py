# FastAPI backend for LifeSyncAI
# Run using fastapi dev

from fastapi import FastAPI, Request, File, UploadFile
from pydantic import BaseModel
from typing import List

import datetime

# Import models
from schemas.academics_absent_schema import AcademicsAbsentData, AcademicsAbsentDataRequest
from schemas.academics_assignment_schema import AcademicsAssignmentData, AcademicsAssignmentDataRequest
from schemas.academics_exam_schema import AcademicsExamData, AcademicsExamDataRequest
from schemas.academics_mark_schema import AcademicsMarkData, AcademicsMarkDataRequest
from schemas.activity_schema import ActivityData, ActivityDataRequest
from schemas.bodymeasurement_schema import BodyMeasurementData, BodyMeasurementDataRequest
from schemas.mind_mood_schema import MindMoodData, MindMoodDataRequest
from schemas.note_schema import NoteData, NoteDataRequest
from schemas.nutrition_schema import NutritionData, NutritionDataRequest
from schemas.symptom_schema import SymptomData, SymptomDataRequest
from schemas.time_schema import TimeData, TimeDataRequest
from schemas.vitals_schema import VitalsData, VitalsDataRequest
from schemas.workout_schema import WorkoutData, WorkoutDataRequest

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

@app.post("/recommendations/academics/absent")
async def read_data_vitals(payload: AcademicsAbsentDataRequest):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    recommendation = [
    ]

    insight = [
    ]

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "academics_absent",
        "score": 67,
        "recommendation": recommendation,
        "insight": insight,
    }

@app.post("/recommendations/academics/assignment")
async def read_data_vitals(payload: AcademicsAssignmentDataRequest):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    recommendation = [
    ]

    insight = [
    ]

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "academics_absent",
        "score": 67,
        "recommendation": recommendation,
        "insight": insight,
    }

@app.post("/recommendations/academics/exam")
async def read_data_vitals(payload: AcademicsExamDataRequest):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    recommendation = [
    ]

    insight = [
    ]

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "academics_exam",
        "score": 67,
        "recommendation": recommendation,
        "insight": insight,
    }

@app.post("/recommendations/academics/mark")
async def read_data_vitals(payload: AcademicsMarkDataRequest):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    recommendation = [
    ]

    insight = [
    ]

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "academics_mark",
        "score": 67,
        "recommendation": recommendation,
        "insight": insight,
    }

@app.post("/recommendations/activity")
async def read_data_vitals(payload: ActivityDataRequest):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    recommendation = [
    ]

    insight = [
    ]

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "activity",
        "score": 67,
        "recommendation": recommendation,
        "insight": insight,
    }

@app.post("/recommendations/bodymeasurement")
async def read_data_vitals(payload: BodyMeasurementDataRequest):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    recommendation = [
    ]

    insight = [
    ]

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "bodymeasurement",
        "score": 67,
        "recommendation": recommendation,
        "insight": insight,
    }

@app.post("/recommendations/mind/mood")
async def read_data_vitals(payload: MindMoodDataRequest):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    recommendation = [
    ]

    insight = [
    ]

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "mind_mood",
        "score": 67,
        "recommendation": recommendation,
        "insight": insight,
    }

@app.post("/recommendations/note")
async def read_data_vitals(payload: NoteDataRequest):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    recommendation = [
    ]

    insight = [
    ]

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "note",
        "score": 67,
        "recommendation": recommendation,
        "insight": insight,
    }

@app.post("/recommendations/symptom")
async def read_data_vitals(payload: SymptomDataRequest):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    recommendation = [
    ]

    insight = [
    ]

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "symptom",
        "score": 67,
        "recommendation": recommendation,
        "insight": insight,
    }

@app.post("/recommendations/time")
async def read_data_vitals(payload: TimeDataRequest):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    recommendation = [
    ]

    insight = [
    ]

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "time",
        "score": 67,
        "recommendation": recommendation,
        "insight": insight,
    }

@app.post("/recommendations/workout")
async def read_data_vitals(payload: WorkoutDataRequest):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    recommendation = [
    ]

    insight = [
    ]

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "workout",
        "score": 67,
        "recommendation": recommendation,
        "insight": insight,
    }

@app.post("/recommendations/vitals")
async def read_data_vitals(payload: VitalsDataRequest):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    recommendation = [
    ]

    insight = [
    ]

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "vitals",
        "score": 67,
        "recommendation": recommendation,
        "insight": insight,
    }

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

@app.post("/upload/nutrition")
async def read_data_vitals(file_upload: UploadFile = File(...)):

    file_uploaded = await file_upload.read()

    # Set file name
    file_name = str(file_upload.filename).replace(" ", "_")
    time_current = str(datetime.datetime.now()).replace(" ", "_")
    file_name_final = "{}_{}".format(time_current, file_name)

    file_path = "uploads/nutrition/{}".format(file_name_final)

    # Save file
    file_handler = open(file_path, "wb")
    file_handler.write(file_uploaded)
    file_handler.close()

    print("File saved")

    return {
        "status": "OK",
        "version": "0.1.0",
        "nutrition_name": "Pizza",
        "nutrition_calories": 167,
    }
