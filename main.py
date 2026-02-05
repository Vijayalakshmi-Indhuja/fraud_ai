from fastapi import FastAPI
from pydantic import BaseModel
from scam_logic import analyze_message
from intelligence import extract_intelligence
from memory import ConversationMemory
from agent import generate_agent_reply
import time

app = FastAPI(title="Fraud AI Honeypot API")

# Global in-memory session (demo purpose)
memory = ConversationMemory()


# -------------------------------
# Root Endpoint (Prevents 404)
# -------------------------------
@app.get("/")
def home():
    return {
        "status": "running",
        "message": "Fraud AI Honeypot is live 🚀",
        "docs": "/docs"
    }


# -------------------------------
# Request Model
# -------------------------------
class MessageInput(BaseModel):
    message: str


# -------------------------------
# Main Analyze Endpoint
# -------------------------------
@app.post("/analyze")
def analyze(data: MessageInput):

    start_time = time.time()

    # 1️⃣ Scam Detection
    scam_result = analyze_message(data.message)

    # 2️⃣ Store scammer message in memory
    memory.add("scammer", data.message)

    agent_reply = None

    # 3️⃣ Activate Honey-Pot if Scam
    if scam_result.get("is_scam"):

        memory_text = memory.get_history_text()

        agent_reply = generate_agent_reply(
            memory_text,
            data.message
        )

        memory.add("agent", agent_reply)

    # 4️⃣ Extract Intelligence
    intelligence = extract_intelligence(data.message)

    duration = int(time.time() - start_time)

    return {
        "scam_detection": scam_result,
        "engagement_metrics": {
            "turns": memory.turns,
            "duration_seconds": duration
        },
        "agent_reply": agent_reply,
        "extracted_intelligence": intelligence
    }
