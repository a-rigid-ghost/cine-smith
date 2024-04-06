import os
import pyttsx3
from constants import GENERATED_MEDIA_FOLDER
from utils.folder_utils import create_directory

def convert_text_to_speech(text: str, rate:int, media_dirname:str, filename: str):
    audio_dir_path = create_directory(media_dirname, "audios") 
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.save_to_file(text, filename=os.path.join(audio_dir_path, filename))
    engine.runAndWait()
    engine.stop()