from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import os
from scam_logic import analyze_message

app = FastAPI()

# Secret key for GUVI validation
GUVI_SECRET = os.getenv("GUVI_SECRET_KEY", "guvi-secret-key")


# -------------------------------
# Root endpoint
# -------------------------------
@app.get("/")
def root():
    return {"message": "Fraud AI Honeypot API is running"}


# -------------------------------
# GUVI VALIDATION ENDPOINT
# -------------------------------
@app.get("/validate")
def validate(x_api_key: str = Header(...)):
    if x_api_key != GUVI_SECRET:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return {
        "status": "active",
        "service": "Fraud AI Honeypot",
        "secure": True
    }


# -------------------------------
# Scam detection endpoint
# -------------------------------
class MessageRequest(BaseModel):
    message: str


@app.post("/analyze")
def analyze(request: MessageRequest, x_api_key: str = Header(...)):
    if x_api_key != GUVI_SECRET:
        raise HTTPException(status_code=401, detail="Unauthorized")

    result = analyze_message(request.message)

    return {
        "scam_detection": result
    }
