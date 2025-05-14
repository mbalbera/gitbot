# streamlit_app.py
import streamlit as st
import requests
import websocket
import threading

st.title("📄 Upload File for AI Processing")

uploaded_file = st.file_uploader("Choose a text file", type=["txt", "md"])
output_area = st.empty()

if uploaded_file and st.button("🚀 Upload and Process"):
    # Upload file to backend
    files = {"file": (uploaded_file.name, uploaded_file, "text/plain")}
    res = requests.post("http://localhost:8000/upload/", files=files)
    session_id = res.json()["session_id"]

    # Start WebSocket to get real-time results
    def on_message(ws, message):
        output_area.text_area("📤 AI Output", value=message, height=300)

    ws = websocket.WebSocketApp(
        f"ws://localhost:8000/ws/{session_id}",
        on_message=on_message
    )

    thread = threading.Thread(target=ws.run_forever)
    thread.start()
