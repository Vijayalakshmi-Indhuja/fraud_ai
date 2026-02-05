import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API Key from environment
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in environment variables")

# Configure Gemini
genai.configure(api_key=api_key)


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

        response = genai.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        # Clean response text
        clean_text = (
            response.text.strip()
            .replace("```json", "")
            .replace("```", "")
        )

        return json.loads(clean_text)

    except Exception as e:
        return {
            "is_scam": None,
            "confidence": 0,
            "reason": f"Error occurred: {str(e)}"
        }
