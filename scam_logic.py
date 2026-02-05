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
    "is_scam": true/false,
    "confidence": percentage number,
    "reason": "short explanation"
}}

Message:
{message}
"""

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt,
        )

        text_output = response.text.strip()

        return json.loads(text_output)

    except Exception as e:
        return {
            "is_scam": None,
            "confidence": 0,
            "reason": f"Error occurred: {str(e)}"
        }
