\# 🛡️ Agentic Honey-Pot for Scam Detection \& Intelligence Extraction



An AI-powered honeypot API that detects scam messages and autonomously engages scammers to extract actionable intelligence.



---



\## 🏗 Built Using



\- FastAPI

\- Google Gemini API

\- Python

\- Regex Intelligence Extraction

\- Multi-turn Conversation Memory



---



\## 🚀 Features



✅ Scam Detection  

✅ Autonomous AI Agent Engagement  

✅ Intelligence Extraction (Bank, UPI, URLs)  

✅ Engagement Metrics Tracking  

✅ Structured JSON API Response  

✅ Production-ready FastAPI deployment  



---



\## 📡 API Endpoint



\*\*POST\*\* `/analyze`



\### 🔹 Request Body



```json

{

&nbsp; "message": "Your bank account is blocked. Click here to verify."

}

🔹 Response Structure

{

&nbsp; "scam\_detection": {

&nbsp;   "is\_scam": true,

&nbsp;   "confidence": 99,

&nbsp;   "reason": "Explanation..."

&nbsp; },

&nbsp; "engagement\_metrics": {

&nbsp;   "turns": 2,

&nbsp;   "duration\_seconds": 5

&nbsp; },

&nbsp; "agent\_reply": "Human-like reply to scammer",

&nbsp; "extracted\_intelligence": {

&nbsp;   "bank\_accounts": \[],

&nbsp;   "upi\_ids": \[],

&nbsp;   "phishing\_links": \[]

&nbsp; }

}

🔐 Environment Variable

Create a .env file:



GEMINI\_API\_KEY=your\_api\_key\_here

▶ Run Locally

uvicorn main:app --reload

Open:



http://127.0.0.1:8000/docs

🌍 Production Deployment

Deployable on Render for hackathon submission.



🏆 Hackathon Submission

Built for:



Agentic Honey-Pot for Scam Detection \& Intelligence Extraction

