# 🎙️ Voice-to-Voice LLM Bot

A real-time conversational assistant that allows users to speak into a microphone, processes the input using speech recognition, generates intelligent responses using a Large Language Model (LLM), and replies back using speech synthesis — all within an interactive Streamlit web interface.

---

## 🚀 Features

- 🎧 **Speech Recognition** using OpenAI's [Whisper](https://github.com/openai/whisper)
- 🧠 **LLM-Based Response Generation** using Gemini/OpenAI/your chosen LLM
- 🔊 **Text-to-Speech (TTS)** with `pyttsx3` for local speech playback
- 💬 **Conversation Memory** displayed in a real-time chat format
- 🌐 **Streamlit UI** for a simple, responsive web interface
- 🛡️ **Repeat Prevention** to avoid duplicate audio outputs
- ⚡ Optimized for faster processing with reduced latency

---

## 📁 Project Structure

```
voice-to-voice-bot/
│
├── app.py                  # Streamlit UI and app logic
├── main.py                 # Audio recording and Whisper transcription
├── llm.py                  # LLM response generation
├── tts.py                  # Text-to-speech handling
├── requirements.txt        # Python dependencies
├── README.md               # Documentation
```

---

## 📦 Requirements

Add this to your `requirements.txt` file:

```
streamlit
openai-whisper
sounddevice
scipy
numpy
torch
pyttsx3
```

Install all at once:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Troubleshooting

- ❗ On **Windows**, you may need [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) for audio-related packages.
- ❗ If audio repeats, ensure `speak()` is only called once per response.
- ❗ Ensure your microphone is functional and allowed in system privacy settings.

---

---

## 📃 License

MIT License. Feel free to use, share, and modify. Attribution appreciated!

---

## 🙌 Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper)
- [Streamlit](https://streamlit.io/)
- [Pyttsx3](https://pyttsx3.readthedocs.io/)
