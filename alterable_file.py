# streamlit_app.py
import streamlit as st
import websocket
import threading
import base64

st.title("📁 Upload File (processed on backend)")

uploaded_file = st.file_uploader("Upload a file", type=["txt", "md"])

if uploaded_file is not None:
    file_bytes = uploaded_file.read()
    encoded = base64.b64encode(file_bytes).decode("utf-8")  # encode for WebSocket transmission

    if st.button("🚀 Send to Backend"):
        output = st.empty()

        def on_message(ws, message):
            output.success(f"✅ Server responded: {message}")

        def on_open(ws):
            ws.send(encoded)

        ws = websocket.WebSocketApp(
            "ws://localhost:8000/ws",
            on_open=on_open,
            on_message=on_message
        )

        thread = threading.Thread(target=ws.run_forever)
        thread.start()
