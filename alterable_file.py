import streamlit as st

# Dummy response function — replace with your actual logic
def get_chat_response(user_input):
    return f"Echo: {user_input}"

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("💬 Chatbot")

# Input + buttons
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", key="user_input")

    col1, col2 = st.columns([1, 1])
    with col1:
        submitted = st.form_submit_button("Submit")
    with col2:
        reset = st.form_submit_button("Reset Memory")

    if submitted and user_input.strip():
        # Append user message
        st.session_state.chat_history.append(("You", user_input))

        # Get bot response
        response = get_chat_response(user_input)
        st.session_state.chat_history.append(("Bot", response))

    if reset:
        st.session_state.chat_history = []
        st.experimental_rerun()

# Display chat history
st.subheader("Chat History")
for speaker, message in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {message}")
