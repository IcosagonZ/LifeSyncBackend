# FastAPI backend for LifeSyncAI
# Run using fastapi dev

from fastapi import FastAPI, Request, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, auth

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed = auth.hash_password(user.password)

    new_user = models.User(username=user.username, password=hashed)
    db.add(new_user)
    db.commit()

    return {"message": "User created"}

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
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


# Vitals data processing
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
        #["Nutrition", "Eat vegetables", "Your consumption of green vegatables is 67% lower than last week"],
        #["Nutrition", "Eat fruits", "Your consumption of fruits is 67% lower than last week"],
    ]

    insight = [
        #["Nutrition", "Carbohydrates increased", "You are eating more carbohydrates than last week"],
    ]

    return {
        "status": "OK",
        "version": "0.1.0",
        "type": "nutrition",
        "score": 67,
        "recommendation": recommendation,
        "insight": insight,
    }
