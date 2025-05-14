clients = {}

async def process_file(session_id, contents, call_nuc_fn):
    ws = clients.get(session_id)
    if not ws:
        return

    async def send_chunk(text):
        if session_id in clients:
            await ws.send_text(text)

    await call_nuc_fn(contents, send_chunk)
    await ws.close()
    clients.pop(session_id, None)
