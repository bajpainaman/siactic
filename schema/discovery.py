# sciatic_protocol/schema/discovery.py

from typing import List, Dict
from pydantic import BaseModel

class Platform(BaseModel):
    id: str
    name: str
    description: str
    models: List[Dict]

class DiscoveryRequest(BaseModel):
    query: str

class DiscoveryResponse(BaseModel):
    platforms: List[Platform]
