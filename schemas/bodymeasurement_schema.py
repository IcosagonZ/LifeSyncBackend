from pydantic import BaseModel
from typing import List

class BodyMeasurementData(BaseModel):
    measurement_type: str
    value: float
    unit: str
    entry_date: str
    entry_note: str

class BodyMeasurementDataRequest(BaseModel):
    version: str
    data: List[BodyMeasurementData]
