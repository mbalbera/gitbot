@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        encoded_data = await websocket.receive_text()
        file_bytes = base64.b64decode(encoded_data)
        
        # Use in-memory file-like object
        file_like = io.BytesIO(file_bytes)
        contents = file_like.read().decode("utf-8")  # or keep as bytes if needed

        result = call_nuc(contents)
        await websocket.send_text(result)
    except Exception as e:
        await websocket.send_text(f"❌ Error: {str(e)}")
    finally:
        await websocket.close()
