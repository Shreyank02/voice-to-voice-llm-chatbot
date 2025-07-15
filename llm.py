from langchain_community.chat_models import ChatOllama
from main import listen_and_transcribe
from tts import speak
from dotenv import load_dotenv

load_dotenv() 

model = ChatOllama(model = 'llama3.2-vision:11b',
             base_url= 'http://91.107.230.57:11434/'
             )

def get_response(prompt: str) -> str:
    try:
        print(f"\nSending to model: {prompt}")
        response = model.invoke(prompt)
        print(f"model response: {response}")

        if isinstance(response, str):
            return response.strip()
        elif hasattr(response, "content"):
            return response.content.strip()
        else:
            return "I'm sorry, I didn't get a valid response."
    except Exception as e:
        print(f"Error generating response from Hugging Face model: {e}")
        return "Sorry, I encountered an error while generating the response."


def voice_to_voice():
    user_input = listen_and_transcribe()
    print(f"Transcribed: {user_input}")

    if not user_input or user_input.strip() == "":
        speak("I didn't catch that. Please try again.")
        return ""

    response = get_response(user_input)
    speak(response)
    return response

def generate_response(user_input: str) -> str:
    if not user_input or user_input.strip() == "":
        return "I didn't catch that. Please try again."

    response_text = get_response(user_input)
    speak(response_text)
    return response_text

if __name__ == "__main__":
    voice_to_voice()
