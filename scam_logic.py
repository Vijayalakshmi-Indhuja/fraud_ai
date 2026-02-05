import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create model instance
model = genai.GenerativeModel("gemini-1.5-flash")


def analyze_message(message: str):
    prompt = f"""
You are a scam detection AI.

Analyze the message below and respond strictly in JSON format:

{{
    "is_scam": true or false,
    "confidence": percentage number,
    "reason": "short explanation"
}}

Message:
{message}
"""

    response = model.generate_content(prompt)

    # Clean response text
    clean_text = (
        response.text.strip()
        .replace("```json", "")
        .replace("```", "")
    )

    try:
        return json.loads(clean_text)
    except:
        return {
            "is_scam": False,
            "confidence": 0,
            "reason": "Failed to parse Gemini response"
        }
