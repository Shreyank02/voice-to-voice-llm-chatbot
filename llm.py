import os
import google.generativeai as genai
from main import listen_and_transcribe
from tts import speak
from dotenv import load_dotenv, dotenv_values

os.environ["PATH"] += os.pathsep + r"C:\Users\Lenovo\Downloads\ffmpeg-7.1.1-essentials_build\bin"

load_dotenv() 
genai.configure(api_key = os.getenv("api_key"))

model = genai.GenerativeModel("gemini-1.5-pro-latest")

def get_response_from_gemini(prompt: str) -> str:
    try:
        print(f"\nSending prompt to Gemini: {prompt}")
        response = model.generate_content(prompt)
        print(f"Gemini raw response: {response}")

        if hasattr(response, "text") and response.text:
            print(f"Gemini responded with: {response.text}")
            return response.text.strip()
        else:
            print("Gemini returned empty or invalid response.")
            return "I'm sorry, I didn't get a valid response."
    except Exception as e:
        print(f"Error generating response from Gemini: {e}")
        return "Sorry, I encountered an error while generating the response."

def voice_to_voice():
    user_input = listen_and_transcribe()
    print(f"Transcribed: {user_input}")

    if not user_input or user_input.strip() == "":
        speak("I didn't catch that. Please try again.")
        return ""

    response = get_response_from_gemini(user_input)
    speak(response)
    return response

def generate_response(user_input: str) -> str:
    if not user_input or user_input.strip() == "":
        return "I didn't catch that. Please try again."

    response_text = get_response_from_gemini(user_input)
    speak(response_text)
    return response_text

if __name__ == "__main__":
    voice_to_voice()
