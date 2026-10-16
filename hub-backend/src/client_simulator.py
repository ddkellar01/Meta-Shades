import asyncio
import websockets
import json

async def simulate_glasses():
    uri = "ws://localhost:8000/ws/telemetry"
    async with websockets.connect(uri) as websocket:
        print("Connected to Meta Shades Hub. Sending test telemetry packet...")
        
        sample_packet = {
            "heart_rate": 78,
            "ecg_peak_ms": 115.5,
            "ppg_peak_ms": 235.0,
            "eeg_raw": [0.2 * (i % 10) for i in range(250)],
            "transcript": "How is my cognitive focus right now?"
        }
        
        await websocket.send(json.dumps(sample_packet))
        response = await websocket.recv()
        print(f"📥 [Hub Response]: {response}")

if __name__ == "__main__":
    asyncio.run(simulate_glasses())
