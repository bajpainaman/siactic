# sciatic_protocol/schema/common.py

from typing import List, Dict
from pydantic import BaseModel

class Context(BaseModel):
    header_info: Dict
    key_lookup: Dict
    encryption: Dict

class Message(BaseModel):
    transaction_info: Dict

class Packet(BaseModel):
    context: Context
    message: Message
