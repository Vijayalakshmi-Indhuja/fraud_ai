import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_agent_reply(memory_text: str, scam_message: str):
    try:
        prompt = f"""
You are a fraud honeypot AI.

You are pretending to be a naive victim.

Conversation so far:
{memory_text}

Scammer just said:
{scam_message}

Respond in a way that keeps the scammer engaged.
Be believable. Do NOT reveal you are an AI.
"""

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception:
        return None
