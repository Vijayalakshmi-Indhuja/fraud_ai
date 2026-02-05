import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in environment variables")

genai.configure(api_key=api_key)

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash-latest")


def generate_agent_reply(memory_text: str, latest_message: str):

    try:
        prompt = f"""
        You are a friendly but intelligent honey-pot agent.

        Your goal is to:
        - Keep the scammer engaged
        - Ask questions
        - Pretend to cooperate
        - Extract more information

        Conversation so far:
        {memory_text}

        Scammer just said:
        {latest_message}

        Generate a natural human-like reply.
        """

        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception as e:
        return f"Agent error: {str(e)}"
