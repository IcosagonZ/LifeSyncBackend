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

class ClientVersion(BaseModel):
    client_version: str

@app.post("/client/version")
async def read_client_version(data: ClientVersion):
    print("Client > Version > {}".format(data.client_version))
    return {
        "status": "OK",
        "version": "0.1.0"
    }
