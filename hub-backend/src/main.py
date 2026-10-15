from fastapi import FastAPI, WebSocket
import json

app = FastAPI(title="Meta Shades Hub Backend")

@app.websocket("/ws/telemetry")
async def telemetry_websocket(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        packet = json.loads(data)
        
        # Echo back processing acknowledgement
        response = {
            "status": "success",
            "received_metrics": list(packet.keys()),
            "alert": False
        }
        await websocket.send_text(json.dumps(response))
