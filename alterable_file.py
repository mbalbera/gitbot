# streamlit_app.py
import streamlit as st
import websocket
import threading
import time

st.set_page_config(layout="wide")
st.title("📁 AI File Interpreter via WebSocket")

messages = st.session_state.get("messages", [])

# Upload file
uploaded_file = st.file_uploader("Upload a text file", type=["txt", "md"])
if uploaded_file is not None:
    file_content = uploaded_file.read().decode("utf-8")
    chunks = [file_content[i:i+500] for i in range(0, len(file_content), 500)]

    st.write(f"🔍 File chunked into {len(chunks)} parts")

    if st.button("🚀 Send to AI"):
        st.session_state["messages"] = []

        def on_message(ws, message):
            st.session_state.messages.append(message)
            st.experimental_rerun()

        def on_open(ws):
            def send_chunks():
                for chunk in chunks:
                    ws.send(chunk)
                    time.sleep(0.1)  # slight delay for realism
            threading.Thread(target=send_chunks).start()

        ws = websocket.WebSocketApp(
            "ws://localhost:8000/ws",
            on_message=on_message,
            on_open=on_open
        )

        threading.Thread(target=ws.run_forever, daemon=True).start()
        st.success("📡 WebSocket connected and chunks sent!")

# Display messages
if st.session_state.get("messages"):
    st.subheader("📨 AI Responses")
    for i, msg in enumerate(st.session_state.messages):
        st.markdown(f"**Chunk {i+1}**: {msg}")
