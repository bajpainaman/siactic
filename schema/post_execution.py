# sciatic_protocol/schema/post_execution.py

from typing import List, Dict
from pydantic import BaseModel

class Feedback(BaseModel):
    model_id: str
    rating: int
    comments: str

class PostExecutionRequest(BaseModel):
    feedback: Feedback

class PostExecutionResponse(BaseModel):
    status: str
    details: Dict
