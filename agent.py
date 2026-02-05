import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create model
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_agent_reply(message: str):

    prompt = f"""
You are pretending to be a normal person responding to a scammer.
Engage naturally and try to extract useful scam intelligence like:

- Bank account numbers
- UPI IDs
- Phone numbers
- Links

Scammer message:
{message}

Respond casually and naturally.
"""

    response = model.generate_content(prompt)

    return response.text.strip()
