import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_agent_reply(memory_text: str, scammer_message: str):

    try:
        prompt = f"""
You are an undercover anti-scam AI honeypot agent.

Conversation history:
{memory_text}

Scammer message:
{scammer_message}

Reply in a way that keeps the scammer engaged but does NOT reveal you are an AI.
"""

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception:
        return None
