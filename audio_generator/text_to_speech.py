import pyttsx3

def convert_text_to_speech(text: str, rate:int, filename: str):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.save_to_file(text, filename=filename)
    engine.runAndWait()
    engine.stop()