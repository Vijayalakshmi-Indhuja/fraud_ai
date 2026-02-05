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

# Create model
model = genai.GenerativeModel("gemini-1.5-flash-latest")


def generate_agent_reply(message: str):

    prompt = f"""
You are an AI honeypot agent.

Your goal is to continue the conversation naturally and extract useful scam intelligence
such as bank details, UPI IDs, phone numbers, phishing URLs, etc.

Scammer message:
{message}
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return f"Error generating agent reply: {str(e)}"
