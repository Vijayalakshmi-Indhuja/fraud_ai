import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_agent_reply(memory_text: str, scam_message: str):
    try:
        prompt = f"""
You are a smart cyber intelligence agent pretending to be a victim.
Keep the scammer engaged.

Conversation history:
{memory_text}

Scammer just said:
{scam_message}

Respond casually and ask a follow-up question.
"""

        response = client.models.generate_content(
            model="gemini-1.0-pro",   # ✅ SAME WORKING MODEL
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"Error generating agent reply: {str(e)}"
