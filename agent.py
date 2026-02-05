import google.generativeai as genai
#from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_agent_reply(message, history):

    prompt = f"""
You are a normal human engaging with a scammer.
Do NOT reveal you are an AI.
Keep the conversation going.
Be curious and slightly confused.

Conversation history:
{history}

Scammer message:
{message}

Reply naturally.
"""

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )

    return response.text
