import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from router import route_assistant_request
from ml_engine.blood_pressure import BloodPressureEstimator
from ml_engine.eeg_processor import EEGProcessor

app = FastAPI(
    title="Meta Shades Unified Hub Backend",
    description="Backend telemetry hub processing sub-surface NIR, EEG mind-reading, and cuffless blood pressure with Google Gemini & Alexa routing.",
    version="1.0.0"
)

# Initialize ML processing engines
bp_estimator = BloodPressureEstimator()
eeg_processor = EEGProcessor(sampling_rate=250)

@app.get("/")
async def root():
    return {
        "status": "online",
        "system": "Meta Shades Hub Backend",
        "endpoints": ["/ws/telemetry"]
    }

@app.websocket("/ws/telemetry")
async def telemetry_websocket(websocket: WebSocket):
    """
    Real-time WebSocket endpoint connecting the ESP32-S3 smart glasses 
    to the hub backend for telemetry processing and AI voice responses.
    """
    await websocket.accept()
    print("🕶️ [WebSocket Connected]: Smart glasses telemetry stream established.")
    
    try:
        while True:
            # Receive raw telemetry packet from ESP32 / Mobile Hub
            raw_data = await websocket.receive_text()
            packet = json.loads(raw_data)
            
            # 1. Extract raw data arrays
            eeg_raw = packet.get("eeg_raw", [0.0] * 250)
            heart_rate = packet.get("heart_rate", 70)
            ecg_peak_ms = packet.get("ecg_peak_ms", 120.0)
            ppg_peak_ms = packet.get("ppg_peak_ms", 240.0)
            user_transcript = packet.get("transcript", None)
            
            # 2. Compute Edge ML Metrics (EEG Brainwave Power Ratios & Focus State)
            eeg_metrics = eeg_processor.extract_band_ratios(eeg_raw)
            
            # 3. Compute Cuffless Blood Pressure via PWTT (Pulse Wave Transit Time)
            pwtt = max(ppg_peak_ms - ecg_peak_ms, 10.0)
            bp_metrics = bp_estimator.estimate_bp(pwtt_ms=pwtt, heart_rate=heart_rate)
            
            # Compile physiological context bundle
            bio_context = {
                "systolic": bp_metrics["systolic"],
                "diastolic": bp_metrics["diastolic"],
                "heart_rate": heart_rate,
                "engagement_index": eeg_metrics["engagement_index"],
                "mental_state": eeg_metrics["state"]
            }
            
            # 4. Route through Hybrid AI Engine if a voice command/query is present
            ai_response_audio = None
            if user_transcript:
                ai_response_audio = await route_assistant_request(user_transcript, bio_context)
            
            # 5. Send computed telemetry and feedback back to the eyewear client
            response_payload = {
                "status": "success",
                "biometrics": bio_context,
                "ai_speech_output": ai_response_audio
            }
            
            await websocket.send_text(json.dumps(response_payload))
            
    except WebSocketDisconnect:
        print("🔌 [WebSocket Disconnected]: Smart glasses session closed.")
    except Exception as e:
        error_payload = {"status": "error", "message": str(e)}
        await websocket.send_text(json.dumps(error_payload))
