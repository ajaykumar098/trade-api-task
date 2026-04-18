import os
from fastapi import Header, HTTPException
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

# In-memory session tracking
sessions = {}


def verify_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")


def track(ip):
    sessions[ip] = sessions.get(ip, 0) + 1


def validate_sector(sector: str):
    if not sector.isalpha() or len(sector) < 3:
        raise HTTPException(status_code=400, detail="Invalid sector name")
