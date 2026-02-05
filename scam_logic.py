import os
import json
from google import genai

# Create Gemini client (safe initialization)
api_key = os.getenv("GEMINI_API_KEY")

client = None
if api_key:
    client = genai.Client(api_key=api_key)


def fallback_analysis(message: str):
    """Rule-based backup detection (works without Gemini)."""
    scam_keywords = [
        "win money",
        "lottery",
        "click this link",
        "urgent",
        "bank details",
        "upi",
        "verify account",
        "free prize"
    ]

    message_lower = message.lower()

    for word in scam_keywords:
        if word in message_lower:
            return {
                "is_scam": True,
                "confidence": 75,
                "reason": "Detected suspicious keywords (rule-based fallback)."
            }

    return {
        "is_scam": False,
        "confidence": 60,
        "reason": "No suspicious keywords detected (rule-based fallback)."
    }


def analyze_message(message: str):
    """
    Hybrid scam detection:
    1) Try Gemini
    2) If error/quota → use fallback logic
    """

    if not client:
        return fallback_analysis(message)

    try:
        prompt = f"""
You are a scam detection AI.

Analyze this message and respond ONLY in JSON format:

{{
  "is_scam": true or false,
  "confidence": number (0-100),
  "reason": "short explanation"
}}

Message:
"{message}"
"""

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        text = response.text.strip()

        # Clean markdown if present
        if text.startswith("```"):
            text = text.split("```")[1]

        return json.loads(text)

    except Exception as e:
        print("Gemini error → using fallback:", str(e))
        return fallback_analysis(message)
