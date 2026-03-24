from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    version: str
    message: str
