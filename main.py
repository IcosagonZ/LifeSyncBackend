# FastAPI backend for LifeSyncAI
# Run using fastapi dev
from fastapi import FastAPI, Request, File, UploadFile, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from pydantic import BaseModel
from typing import List
import datetime

# LLM interfacing
from openai import OpenAI

# Import local libraries
import LifeSyncBackend.models, LifeSyncBackend.schemas, LifeSyncBackend.auth
from LifeSyncBackend.auth import SECRET_KEY, ALGORITHM
from LifeSyncBackend.database import SessionLocal, engine

# Import models
from LifeSyncBackend.schemas.all_schema import AllDataRequest
from LifeSyncBackend.schemas.chat_schema import ChatRequest


from LifeSyncBackend.schemas.academics_absent_schema import AcademicsAbsentData, AcademicsAbsentDataRequest
from LifeSyncBackend.schemas.academics_assignment_schema import AcademicsAssignmentData, AcademicsAssignmentDataRequest
from LifeSyncBackend.schemas.academics_exam_schema import AcademicsExamData, AcademicsExamDataRequest
from LifeSyncBackend.schemas.academics_mark_schema import AcademicsMarkData, AcademicsMarkDataRequest
from LifeSyncBackend.schemas.activity_schema import ActivityData, ActivityDataRequest
from LifeSyncBackend.schemas.bodymeasurement_schema import BodyMeasurementData, BodyMeasurementDataRequest
from LifeSyncBackend.schemas.mind_mood_schema import MindMoodData, MindMoodDataRequest
from LifeSyncBackend.schemas.note_schema import NoteData, NoteDataRequest
from LifeSyncBackend.schemas.nutrition_schema import NutritionData, NutritionDataRequest
from LifeSyncBackend.schemas.symptom_schema import SymptomData, SymptomDataRequest
from LifeSyncBackend.schemas.time_schema import TimeData, TimeDataRequest
from LifeSyncBackend.schemas.vitals_schema import VitalsData, VitalsDataRequest
from LifeSyncBackend.schemas.workout_schema import WorkoutData, WorkoutDataRequest
from LifeSyncBackend.schemas.user_schema import UserCreate, UserLogin

# Import analyzers
from LifeSyncBackend.analyzer.academics_absent_analyzer import academics_absent_analyzer
from LifeSyncBackend.analyzer.academics_assignment_analyzer import academics_assignment_analyzer
from LifeSyncBackend.analyzer.academics_exam_analyzer import academics_exam_analyzer
from LifeSyncBackend.analyzer.academics_mark_analyzer import academics_mark_analyzer
from LifeSyncBackend.analyzer.activity_analyzer import activity_analyzer
from LifeSyncBackend.analyzer.all_analyzer import all_analyzer
from LifeSyncBackend.analyzer.bodymeasurement_analyzer import bodymeasurement_analyzer
from LifeSyncBackend.analyzer.mind_mood_analyzer import mind_mood_analyzer
from LifeSyncBackend.analyzer.note_analyzer import note_analyzer
from LifeSyncBackend.analyzer.nutrition_analyzer import nutrition_analyzer
from LifeSyncBackend.analyzer.symptom_analyzer import symptom_analyzer
from LifeSyncBackend.analyzer.time_analyzer import time_analyzer
from LifeSyncBackend.analyzer.vitals_analyzer import vitals_analyzer
from LifeSyncBackend.analyzer.workout_analyzer import workout_analyzer

app = FastAPI()

openai_client = OpenAI(
    base_url="http://localhost:1337/v1",
    api_key="not-needed"
)
openai_model = "janhq/Jan-v3-4b-base-instruct-Q4_K_XL"
openai_system = '''
Role: You are a specialized Health & Wellness Assistant for students.
Constraint 0: Answer in 5-6 sentences max.
Constraint 1: You ONLY answer questions related to physical health, mental well-being, sleep, nutrition, and academic stress management.
Constraint 2: If a user asks about unrelated topics (e.g., coding, history, politics, or general trivia), you must politely decline and pivot back to health.
Constraint 3: CRITICAL: You are an AI, not a doctor. Every response regarding symptoms must include a disclaimer to consult a professional.
Constraint 4: If a user mentions self-harm or a crisis, provide immediate emergency resources (e.g., [Local Helpline Number]).
'''

LifeSyncBackend.models.Base.metadata.create_all(bind=engine)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token validation error",
        headers={"WWW-Authenticate":"Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if(user_id is None):
            raise credentials_exception
        return user_id
    except JWTError:
        raise credentials_exception



@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(LifeSyncBackend.models.User).filter(LifeSyncBackend.models.User.username == user.username).first()
    if existing:
        #raise HTTPException(status_code=400, detail="User already exists")
        return {
            "status": "ERROR",
            "version": "0.1.0",
            "message": "User already exists"
        }

    hashed = LifeSyncBackend.auth.hash_password(user.password)

    new_user = LifeSyncBackend.models.User(username=user.username, password=hashed)
    db.add(new_user)
    db.commit()

    return {
        "status": "OK",
        "version": "0.1.0",
        "message": "User created"
    }

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(LifeSyncBackend.models.User).filter(LifeSyncBackend.models.User.username == user.username).first()

    print(f"Got {user}")

    if(not db_user or not LifeSyncBackend.auth.verify_password(user.password, db_user.password)):
        #raise HTTPException(status_code=401, detail="Invalid credentials")
        print("User doesnt exist")
        return{
            "status": "ERROR",
            "version": "0.1.0",
            "message": "Invalid username/password",
        }
    else:
        print("User exist")
        token = LifeSyncBackend.auth.create_token({"sub": user.username})

        return{
            "status": "OK",
            "version": "0.1.0",
            "message": "Login success",
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

@app.post("/chat")
async def read_chat_request(request: ChatRequest):
    try:
        response = openai_client.chat.completions.create(
            model=openai_model,
            messages=[
                {"role":"system", "content": openai_system},
                {"role":"user", "content": request.message},
            ],
            temperature=0.5

        )
        return {
            "status": "OK",
            "version": "0.1.0",
            "message": response.choices[0].message.content
        }
    except Exception as e:
        return {
            "status": "ERROR",
            "version": "0.1.0",
            "message": str(e)
        }

@app.post("/insights/academics/absent")
async def read_data_academics_absent(payload: AcademicsAbsentDataRequest, current_user: str = Depends(get_current_user)):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    [insight, score] = academics_absent_analyzer(payload.data)

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "academics_absent",
        "score": 67,
        "insight": insight,
    }

@app.post("/insights/academics/assignment")
async def read_data_academics_assignment(payload: AcademicsAssignmentDataRequest, current_user: str = Depends(get_current_user)):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    [insight, score] = academics_assignment_analyzer(payload.data)

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "academics_absent",
        "score": score,
        "insight": insight,
    }

@app.post("/insights/academics/exam")
async def read_data_academics_exam(payload: AcademicsExamDataRequest, current_user: str = Depends(get_current_user)):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    [insight, score] = academics_exam_analyzer(payload.data)

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "academics_exam",
        "score": score,
        "insight": insight,
    }

@app.post("/insights/academics/mark")
async def read_data_academics_mark(payload: AcademicsMarkDataRequest, current_user: str = Depends(get_current_user)):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    [insight, score] = academics_mark_analyzer(payload.data)

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "academics_mark",
        "score": score,
        "insight": insight,
    }

@app.post("/insights/activity")
async def read_data_activity(payload: ActivityDataRequest, current_user: str = Depends(get_current_user)):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    [insight, score] = activity_analyzer(payload.data)

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "activity",
        "score": score,
        "insight": insight,
    }

@app.post("/insights/bodymeasurement")
async def read_data_bodymeasurement(payload: BodyMeasurementDataRequest, current_user: str = Depends(get_current_user)):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    [insight, score] = bodymeasurement_analyzer(payload.data)

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "bodymeasurement",
        "score": score,
        "insight": insight,
    }

@app.post("/insights/mind/mood")
async def read_data_mind_mood(payload: MindMoodDataRequest, current_user: str = Depends(get_current_user)):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    [insight, score] = mind_mood_analyzer(payload.data)

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "mind_mood",
        "score": score,
        "insight": insight,
    }

@app.post("/insights/note")
async def read_data_note(payload: NoteDataRequest, current_user: str = Depends(get_current_user)):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    [insight, score] = note_analyzer(payload.data)

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "note",
        "score": score,
        "insight": insight,
    }

@app.post("/insights/symptom")
async def read_data_symptom(payload: SymptomDataRequest, current_user: str = Depends(get_current_user)):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    [insight, score] = symptom_analyzer(payload.data)

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "symptom",
        "score": score,
        "insight": insight,
    }

@app.post("/insights/time")
async def read_data_time(payload: TimeDataRequest, current_user: str = Depends(get_current_user)):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    [insight, score] = time_analyzer(payload.data)

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "time",
        "score": score,
        "insight": insight,
    }

@app.post("/insights/workout")
async def read_data_workout(payload: WorkoutDataRequest, current_user: str = Depends(get_current_user)):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    [insight, score] = workout_analyzer(payload.data)

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "workout",
        "score": score,
        "insight": insight,
    }

@app.post("/insights/vitals")
async def read_data_vitals(payload: VitalsDataRequest, current_user: str = Depends(get_current_user)):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    [insight, score] = vitals_analyzer(payload)

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "vitals",
        "score": score,
        "insight": insight,
    }

@app.post("/insights/nutrition")
async def read_data_nutrition(payload: NutritionDataRequest, current_user: str = Depends(get_current_user)):
    #print("Client>Version: {}".format(payload.version))
    #print("Client>Data: Received {} rows".format(len(payload.data)))

    [insight, score] = nutrition_analyzer(payload.data)

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "nutrition",
        "score": score,
        "insight": insight,
    }

@app.post("/insights/all")
async def read_data_all(payload: AllDataRequest, current_user: str = Depends(get_current_user)):
    print("Client>User: {}".format(current_user))
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received all data")

    insights, scores = all_analyzer(payload)

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "vitals",
        "scores": scores,
        "insight": insights,
    }

@app.post("/upload/nutrition")
async def read_image_nutrition(file_upload: UploadFile = File(...), current_user: str = Depends(get_current_user)):

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
