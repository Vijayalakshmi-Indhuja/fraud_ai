from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from scam_logic import analyze_message

app = FastAPI()

API_SECRET = "guvi-secret-key"  # must match what you enter in GUVI popup


# ✅ Root GET endpoint (GUVI tester will hit this)
@app.get("/")
def health_check(x_api_key: str = Header(...)):
    if x_api_key != API_SECRET:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    return {
        "status": "success",
        "message": "Honeypot API is reachable and secure"
    }


# ✅ Analyze endpoint
class MessageRequest(BaseModel):
    message: str


@app.post("/analyze")
def analyze(request: MessageRequest, x_api_key: str = Header(...)):
    if x_api_key != API_SECRET:
        raise HTTPException(status_code=401, detail="Invalid API key")

    result = analyze_message(request.message)
    return result
