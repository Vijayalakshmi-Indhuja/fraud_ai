# 🛡️ Agentic Honey-Pot for Scam Detection & Intelligence Extraction

An AI-powered honeypot API that detects scam messages and autonomously engages scammers to extract actionable intelligence such as bank accounts, UPI IDs, and phishing URLs.

---

## 🚀 Built Using

- FastAPI
- Google Gemini API
- Python
- Regex-based Intelligence Extraction
- Multi-turn Conversation Memory

---

## ✨ Features

- ✅ Scam Detection
- ✅ Autonomous AI Agent Engagement
- ✅ Intelligence Extraction (Bank Accounts, UPI IDs, URLs)
- ✅ Engagement Metrics Tracking
- ✅ Structured JSON API Response
- ✅ Production-ready FastAPI deployment

---

## 📡 API Endpoint

### POST `/analyze`

---

### 🔹 Request Body

```json
{
  "message": "Your bank account is blocked. Click here to verify."
}
```

---

### 🔹 Response Structure

```json
{
  "scam_detection": {
    "is_scam": true,
    "confidence": 99,
    "reason": "Explanation of why this message is a scam"
  },
  "engagement_metrics": {
    "turns": 2,
    "duration_seconds": 5
  },
  "agent_reply": "Human-like response engaging the scammer",
  "extracted_intelligence": {
    "bank_accounts": [],
    "upi_ids": [],
    "phishing_links": []
  }
}
```

---

## 🔐 Environment Variable

Create a `.env` file in your project root:

```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶ Run Locally

```bash
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🌍 Production Deployment

This project is deployment-ready and can be hosted on:

- Render
- Railway
- Fly.io
- Any cloud supporting FastAPI

---

## 🏆 Hackathon Submission

Built for:

**Agentic Honey-Pot for Scam Detection & Intelligence Extraction**

An AI-driven system that:
- Detects scam intent
- Engages scammers autonomously
- Extracts actionable fraud intelligence
- Tracks engagement metrics
- Returns structured intelligence output

---

## 📂 Project Structure

```
fraud_ai/
│── main.py
│── agent.py
│── scam_logic.py
│── intelligence.py
│── memory.py
│── requirements.txt
│── .env
│── .gitignore
│── README.md
```

---

## 👩‍💻 Author

Vijayalakshmi

