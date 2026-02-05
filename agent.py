import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in environment variables")

# Configure Gemini
genai.configure(api_key=api_key)

# Use supported model
model = genai.GenerativeModel("gemini-1.0-pro")


def generate_agent_reply(memory_text: str, latest_message: str):
    try:
        prompt = f"""
You are an AI honeypot agent.

Your job is to engage scammers naturally and try to extract useful intelligence
such as bank details, UPI IDs, phishing links, or phone numbers.

Conversation so far:
{memory_text}

Scammer's latest message:
{latest_message}

Respond naturally as a potential victim.
"""

        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception as e:
        return f"Error generating agent reply: {str(e)}"
