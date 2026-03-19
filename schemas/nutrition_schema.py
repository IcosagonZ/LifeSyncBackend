from pydantic import BaseModel
from typing import List

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
