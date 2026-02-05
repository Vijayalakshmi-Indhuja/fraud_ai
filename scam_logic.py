import os
import json
from google import genai

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_message(message: str):
    try:
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

        response = client.models.generate_content(
            model="gemini-2.0-flash"
            contents=prompt
        )

        text = response.text.strip()

        # Clean markdown if Gemini wraps it
        text = text.replace("```json", "").replace("```", "").strip()

        return json.loads(text)

    except Exception as e:
        return {
            "is_scam": None,
            "confidence": 0,
            "reason": f"Error occurred: {str(e)}"
        }
