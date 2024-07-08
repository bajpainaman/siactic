# sciatic_protocol/schema/transaction.py

from typing import List, Dict
from pydantic import BaseModel

class TrainingRequest(BaseModel):
    model_id: str
    parameters: Dict

class InferenceRequest(BaseModel):
    model_id: str
    input_data: Dict

class TransactionResponse(BaseModel):
    status: str
    details: Dict
