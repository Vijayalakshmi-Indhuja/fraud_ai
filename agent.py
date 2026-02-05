import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_agent_reply(memory_text: str, latest_message: str):

    prompt = f"""
You are an undercover AI agent interacting with a scammer.
Your goal is to waste the scammer’s time while sounding realistic.

Conversation history:
{memory_text}

Latest scammer message:
{latest_message}

Respond naturally.
"""

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt,
    )

    return response.text
