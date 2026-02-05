from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_message(message: str):

    prompt = f"""
    You are a scam detection AI.

    Analyze the message below and respond in JSON format:

    {{
        "is_scam": true/false,
        "confidence": percentage number,
        "reason": "short explanation"
    }}

    Message:
    {message}
    """

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )

    import json
    clean_text = response.text.strip().replace("```json", "").replace("```", "")
    return json.loads(clean_text)
