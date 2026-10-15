from google import genai
from google.genai import types
import os

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def query_gemini_multimodal(prompt: str, telemetry_context: str = "") -> str:
    full_prompt = f"{telemetry_context}\nUser Inquiry: {prompt}" if telemetry_context else prompt
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=full_prompt,
        config=types.GenerateContentConfig(
            temperature=0.3,
            max_output_tokens=150
        )
    )
    return response.text
