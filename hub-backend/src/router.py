import asyncio
from gemini_client import query_gemini_multimodal
from alexa_client import send_to_alexa

async def route_assistant_request(transcript: str, bio_context: dict):
    iot_keywords = ["light", "turn on", "turn off", "music", "thermostat"]
    
    if any(word in transcript.lower() for word in iot_keywords):
        return await send_to_alexa(transcript)
    else:
        prompt = f"User Query: '{transcript}'. Current State: SBP={bio_context.get('sbp')}, Focus={bio_context.get('state')}."
        return await query_gemini_multimodal(prompt)
