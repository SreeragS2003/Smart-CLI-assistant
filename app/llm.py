import os
from dotenv import load_dotenv
import google.genai as genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are a structured AI assistant.

STRICT RULES:
- Output ONLY valid JSON
- No extra text before or after
- No explanations outside JSON

Format:
{
  "answer": "...",
  "reasoning": "...",
  "confidence": "low | medium | high"
}
"""

def ask_llm(query):
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=SYSTEM_PROMPT + "\nUser: " + query,
        config={
            "temperature": 0.3
        }
    )

    return response.text