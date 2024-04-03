import pyttsx3

def convert_test_to_speech(text: str, rate:int):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.save_to_file(text, 'speech.mp3')
    engine.runAndWait()
    engine.stop()