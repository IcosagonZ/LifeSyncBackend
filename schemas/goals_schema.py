from pydantic import BaseModel

class GoalsData(BaseModel):
    height:int
    weight:int
    age:int
    gender:str

    steps:int
    distance:int
    calories:int

    study:int
    sleep:int
    exercise:int
