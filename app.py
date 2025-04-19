import streamlit as st
from main import listen_and_transcribe
from llm import generate_response
from tts import speak

st.set_page_config(page_title="Voice-to-Voice LLM Bot", layout="centered")
st.title("Voice-to-Voice LLM Bot")
st.markdown("### Speak into your mic and interact with the LLM")

if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []
if 'last_response' not in st.session_state:
    st.session_state['last_response'] = ""

if st.button("🎤 Start Talking"):
    with st.spinner("Listening..."):
        user_input = listen_and_transcribe()
        st.write("🗣️ You said:", user_input)

    if user_input:
        st.session_state['conversation'].append(("You", user_input))

        with st.spinner("Thinking..."):
            response = generate_response(user_input)

            if response != st.session_state['last_response']:
                st.session_state['conversation'].append(("Bot", response))
                speak(response)
                st.session_state['last_response'] = response
            else:
                st.write("🤖 Bot skipped repeating the same response.")

st.markdown("### Conversation")
for speaker, text in st.session_state['conversation']:
    st.markdown(f"**{speaker}:** {text}")
