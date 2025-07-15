import streamlit as st
import tempfile
from main import listen_and_transcribe
from llm import generate_response
from tts import speak
from rag import load_document, build_rag_chain

st.set_page_config(page_title="Voice-to-Voice LLM Bot", layout="centered")
st.title("Voice-to-Voice LLM Bot")
st.markdown("### Speak into your mic and interact with the Bot")

if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []
if 'last_response' not in st.session_state:
    st.session_state['last_response'] = ""
if 'rag_chain' not in st.session_state:
    st.session_state['rag_chain'] = None

# Document upload
uploaded_file = st.file_uploader("Upload a document (PDF, TXT, DOCX) to enable RAG", type=["pdf", "txt", "docx"])

# RAG toggle
use_rag = st.checkbox("Use RAG (Retrieval-Augmented Generation)")

# Load RAG chain if file uploaded
if uploaded_file and st.session_state['rag_chain'] is None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name
    ext = uploaded_file.name.split(".")[-1]
    with st.spinner("Processing document...it may take some time..."):
        docs = load_document(tmp_path, ext)
        st.session_state['rag_chain'] = build_rag_chain(docs)
    st.success("Document loaded and indexed for RAG.")

if st.button("Start Talking"):
    with st.spinner("Listening..."):
        user_input = listen_and_transcribe()
        st.write("You said:", user_input)

    if user_input:
        st.session_state['conversation'].append(("You", user_input))

        with st.spinner("Thinking..."):
            if use_rag and st.session_state['rag_chain']:
                try:
                    response = st.session_state['rag_chain'].run(user_input)
                except Exception as e:
                    response = "RAG failed. " + str(e)
            else:
                response = generate_response(user_input)

            if response != st.session_state['last_response']:
                st.session_state['conversation'].append(("Bot", response))
                speak(response)
                st.session_state['last_response'] = response
            else:
                st.write("Bot skipped repeating the same response.")

st.markdown("### Conversation")
for speaker, text in st.session_state['conversation']:
    st.markdown(f"**{speaker}:** {text}")
