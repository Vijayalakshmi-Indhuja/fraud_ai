from fastapi import FastAPI
from pydantic import BaseModel
from scam_logic import analyze_message
from intelligence import extract_intelligence
from memory import ConversationMemory
from agent import generate_agent_reply
import time

app = FastAPI()

memory = ConversationMemory()

class MessageInput(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "Fraud AI Honeypot API is running"}

@app.post("/analyze")
def analyze(data: MessageInput):

    start_time = time.time()

    scam_result = analyze_message(data.message)

    memory.add("scammer", data.message)

    agent_reply = None

    if scam_result.get("is_scam"):

        memory_text = memory.get_history_text()

        agent_reply = generate_agent_reply(
            memory_text,
            data.message
        )

        memory.add("agent", agent_reply)

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
