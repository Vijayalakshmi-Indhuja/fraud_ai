import os
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from scam_logic import analyze_message

app = FastAPI()

# 🔐 Set your hackathon API key here
HACKATHON_API_KEY = os.getenv("HACKATHON_API_KEY", "guvi-secret-key")


# Request model
class MessageRequest(BaseModel):
    message: str


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Fraud AI Honeypot API is running"}


# Analyze endpoint (Protected)
@app.post("/analyze")
def analyze(request: MessageRequest, x_api_key: str = Header(None)):

    # 🔐 Validate API key
    if x_api_key != HACKATHON_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    result = analyze_message(request.message)

    return {
        "scam_detection": result,
        "engagement_metrics": {
            "turns": 1,
            "duration_seconds": 0
        },
        "agent_reply": None,
        "extracted_intelligence": {
            "bank_accounts": [],
            "upi_ids": [],
            "phishing_links": []
        }
    }
