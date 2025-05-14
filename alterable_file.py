# server.py
from fastapi import FastAPI, File, UploadFile, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import uuid
import asyncio

app = FastAPI()

# Let Streamlit frontend connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

clients = {}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    session_id = str(uuid.uuid4())
    contents = await file.read()

    # Start processing in background
    asyncio.create_task(process_file(session_id, contents))

    return {"session_id": session_id}

@app.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await websocket.accept()
    clients[session_id] = websocket

    try:
        while True:
            await asyncio.sleep(1)  # keep alive
    except:
        pass
    finally:
        clients.pop(session_id, None)

async def process_file(session_id: str, contents: bytes):
    # Simulated chunked AI processing
    text = contents.decode("utf-8")
    lines = text.splitlines()

    ws = clients.get(session_id)
    if not ws:
        return

    for i, line in enumerate(lines):
        await asyncio.sleep(0.5)  # simulate work
        if session_id in clients:
            await ws.send_text(f"Chunk {i+1}: {line}")

    await ws.send_text("✅ Done processing!")
    await ws.close()
