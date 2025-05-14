# fastapi_server.py
from fastapi import FastAPI, WebSocket
import uvicorn
import asyncio

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            chunk = await websocket.receive_text()
            # Simulate AI parsing
            await asyncio.sleep(0.5)
            parsed = f"AI interpretation of: {chunk[:50]}..."
            await websocket.send_text(parsed)
        except Exception as e:
            print("WebSocket closed:", e)
            break

if __name__ == "__main__":
    uvicorn.run("fastapi_server:app", host="0.0.0.0", port=8000)
