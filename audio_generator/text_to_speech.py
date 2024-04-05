import os
import pyttsx3
from constants import GENERATED_MEDIA_FOLDER

def convert_text_to_speech(text: str, rate:int, filename: str):
    audio_dir_path = make_audio_folder()
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.save_to_file(text, filename=os.path.join(audio_dir_path, filename))
    engine.runAndWait()
    engine.stop()

def make_audio_folder():
    audio_dir_path = os.path.join(os.getcwd(), GENERATED_MEDIA_FOLDER, "audios")
    if not os.path.exists(audio_dir_path):
        os.makedirs(audio_dir_path)
    return audio_dir_path