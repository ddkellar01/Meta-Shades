from gemini_client import query_gemini_multimodal
from alexa_client import send_to_alexa

async def route_assistant_request(transcript: str, bio_context: dict) -> str:
    """
    Intelligent Assistant Router:
    - Smart home / IoT commands -> Alexa Voice Service
    - Health coaching, vision reasoning, & neural states -> Google Gemini
    """
    iot_keywords = ["light", "turn on", "turn off", "music", "thermostat", "volume", "alexa"]
    
    if any(keyword in transcript.lower() for keyword in iot_keywords):
        return await send_to_alexa(transcript)
    else:
        prompt = f"User Query: '{transcript}'. Telemetry: SBP={bio_context.get('sbp')}, Focus={bio_context.get('state')}."
        return await query_gemini_multimodal(prompt)
