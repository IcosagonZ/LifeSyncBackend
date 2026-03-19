from pydantic import BaseModel
from typing import List

class VitalsData(BaseModel):
  type: str
  value: str
  unit: str
  entry_date: str
  entry_note: str

class VitalsDataRequest(BaseModel):
    version: str
    data: List[VitalsData]
