# sciatic_protocol/schema/execution.py

from typing import List, Dict
from pydantic import BaseModel

class ProgressUpdate(BaseModel):
    task_id: str
    progress: int

class ExecutionRequest(BaseModel):
    task_id: str

class ExecutionResponse(BaseModel):
    status: str
    progress_updates: List[ProgressUpdate]
