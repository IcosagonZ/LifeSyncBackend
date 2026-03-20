# FastAPI backend for LifeSyncAI
# Run using fastapi dev
from fastapi import FastAPI, Request, File, UploadFile, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, auth
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
from schemas.user_schema import UserCreate, UserLogin

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed = auth.hash_password(user.password)

    new_user = models.User(username=user.username, password=hashed)
    db.add(new_user)
    db.commit()

    return {"message": "User created"}

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()

    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = auth.create_token({"sub": user.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }

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
    #print("Client>Version: {}".format(payload.version))
    #print("Client>Data: Received {} rows".format(len(payload.data)))

    recommendation = [
    ]

    insight = [
    ]

    user_weight = 64 #kg
    user_height = 170 #cm
    user_age = 21
    user_gender = "M"
    user_activity = "lightly_active"

    # Calculate calories needed
    user_basal_metabolic_rate = 10 * user_weight + 6.25 * user_height - 5.0 * user_age
    if(user_gender=="F"):
        user_basal_metabolic_rate -= 161
    else:
        user_basal_metabolic_rate += 5
    '''
    If you are sedentary (little or no exercise) : Calorie-Calculation = BMR x 1.2
    If you are lightly active (light exercise/sports 1-3 days​/week) : Calorie-Calculation = BMR x 1.375
    If you are moderately active (moderate exercise/sports 3-5 days/week) : Calorie-Calculation = BMR x 1.55
    If you are very active (hard exercise/sports 6-7 days a week) : Calorie-Calculation = BMR x 1.725
    If you are extra active (very hard exercise/sports & physical job or 2x training) : Calorie-Calculation = BMR x 1.9
    '''
    total_calories_multiplier = {
        "sedentary":1.2,
        "lightly_active":1.375,
        "moderately_active":1.55,
        "very_active":1.725,
        "extra_active":1.9,
    }
    user_total_calorie_needs = user_basal_metabolic_rate * total_calories_multiplier[user_activity]

    # Add up calories, proteins, fats, carbohydrates (assuming same day)
    total_calories = 0
    total_carbs = 0
    total_fats = 0
    total_proteins = 0
    nutrition_data = payload.data
    for item in nutrition_data:
        total_calories += item.calories
        total_carbs += item.carbs
        total_fats += item.fats
        total_proteins += item.protein

    # Energy requirements
    if(abs(total_calories-user_total_calorie_needs)<100):
        insight.append(["Nutrition", "Meeting daily energy requirements", "You are meeting your daily energy requirements of {} cal".format(user_total_calorie_needs)])
    elif(total_calories<user_total_calorie_needs):
        recommendation.append(["Nutrition", "Consuming less than energy requirements", "You are not meeting your daily energy requirements of {} cal".format(user_total_calorie_needs)])
    else:
        recommendation.append(["Nutrition", "Consuming more than energy requirements", "You are eating more than your daily energy requirements of {} cal".format(user_total_calorie_needs)])

    # Carb requirements
    user_carbs = 130
    if(abs(total_carbs-user_carbs)<10):
        insight.append(["Nutrition", "Meeting carbohydrate requirements", "You are meeting your daily carbohydrate requirements of {} g".format(user_carbs)])
    elif(total_calories<user_carbs):
        recommendation.append(["Nutrition", "Short of carbohydrate requirements", "You are not meeting your daily carbohydrate requirements of {} g".format(user_carbs)])
    else:
        recommendation.append(["Nutrition", "Short of carbohydrate requirements", "You are consuming more than your daily carbohydrate requirements of {} g".format(user_carbs)])

    # Fat requirements
    user_fats_lower = user_total_calorie_needs*0.2
    user_fats_high = user_total_calorie_needs*0.35

    if(total_fats>user_fats_lower and total_fats<user_fats_high):
        insight.append(["Nutrition", "Meeting fat requirements", "You are meeting your daily fat requirements of {} g to {} g".format(user_fats_lower, user_fats_high)])
    elif(total_fats<user_fats_lower):
        recommendation.append(["Nutrition", "Short of fat requirements", "You are not meeting your fat requirements of {} g to {} g".format(user_fats_lower, user_fats_high)])
    else:
        recommendation.append(["Nutrition", "Short of fat requirements", "You are consuming more than your daily fat requirements of {} g to {} g".format(user_fats_lower, user_fats_high)])

    # Protein requirements
    protein_requirement = {
        "M":56,
        "F":46
    }
    user_proteins = protein_requirement[user_gender]
    if(abs(total_fats-user_proteins)<10):
        insight.append(["Nutrition", "Meeting protein requirements", "You are meeting your daily protein requirements of {} g".format(user_proteins)])
    elif(total_calories<user_proteins):
        recommendation.append(["Nutrition", "Short of protein requirements", "You are not meeting your daily protein requirements of {} g".format(user_proteins)])
    else:
        recommendation.append(["Nutrition", "Short of protein requirements", "You are consuming more than your daily protein requirements of {} g".format(user_proteins)])

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
