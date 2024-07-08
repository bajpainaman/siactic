# sciatic_protocol/config.py

import os

class Config:
    DEBUG = True
    SECRET_KEY = os.urandom(24)
