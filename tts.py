import pyttsx3
import tempfile
import os
import pygame

def speak(text: str):
    if not text.strip():
        return

    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tf:
        temp_filename = tf.name

    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.save_to_file(text, temp_filename)
    engine.runAndWait()

    pygame.mixer.init()
    pygame.mixer.music.load(temp_filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()
    os.remove(temp_filename)
