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

@app.post("/data/vitals")
async def read_data_vitals(payload: VitalsDataRequest):
    print("Client>Version: {}".format(payload.version))
    print("Client>Data: Received {} rows".format(len(payload.data)))

    return {
        "status": "OK",
        "version": "0.1.0"
    }
