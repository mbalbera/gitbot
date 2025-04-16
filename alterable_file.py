import streamlit as st

# Dummy response function — replace with your actual logic
def get_chat_response(user_input):
    return f"Echo: {user_input}"

# Initialize chat history in session state
if "chathistory" not in st.session_state:
    st.session_state.chathistory = []

st.title("💬 Chatbot")

# Input area
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", key="user_input")
    submitted = st.form_submit_button("Submit")

    if submitted and user_input.strip():
        # Append user message
        st.session_state.chathistory.append(("You", user_input))

        # Get bot response
        response = get_chat_response(user_input)
        st.session_state.chathistory.append(("Bot", response))

# Display chat history
st.subheader("Chat History")
for speaker, message in st.session_state.chathistory:
    st.markdown(f"**{speaker}:** {message}")

# Reset button
if st.button("Reset Memory"):
    st.session_state.chathistory = []
    st.experimental_rerun()

