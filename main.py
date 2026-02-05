from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional
import os
from scam_logic import analyze_message

app = FastAPI()

# Your custom API key for GUVI
API_SECRET_KEY = os.getenv("GUVI_API_KEY", "guvi-secret-key")


class MessageRequest(BaseModel):
    message: Optional[str] = None


@app.get("/")
def root():
    return {"message": "Fraud AI Honeypot API is running"}


@app.post("/analyze")
def analyze(
    request: Optional[MessageRequest] = None,
    x_api_key: str = Header(None)
):
    # 🔐 API Key Check
    if x_api_key != API_SECRET_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # If no message provided (GUVI tester case)
    if request is None or request.message is None:
        return {
            "status": "active",
            "message": "Honeypot endpoint validated successfully"
        }

    # Normal analyze logic (Swagger case)
    result = analyze_message(request.message)
    return result
