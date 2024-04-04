import os

from text_generator.dialogue_creator import get_dialogue
from text_generator.constants import OPENAI_API_KEY

from audio_generator.text_to_speech import convert_text_to_speech

from mutagen.wave import WAVE 

# Login -> https://platform.openai.com/api-keys -> Generate Key -> Replace here
os.environ[OPENAI_API_KEY] = "<YOUR_API_KEY>"
IDEA_PROMPT = "Top 10 Places to visit in Schengen Area"
AUDIO_SPEED = 200

def main():
    dirname = os.path.dirname(__file__)

    print("Starting Text Generation...")
    # For actual ChatGPT invocation to generate dialogue
    # dialogue = get_dialogue(idea_prompt=IDEA_PROMPT) 

    # For Mock dialogue generation
    dialogue = open(os.path.join(dirname, 'data/sample_chatgpt_response.txt'), "r").read()

    print("Text Generation complete.")
    print(f"Dialogue: {dialogue}")
    
    print("Starting Audio Generation...")

    audio_filename = f"audio_file_{IDEA_PROMPT}.mp3"
    convert_text_to_speech(dialogue, AUDIO_SPEED, audio_filename)

    print("Audio Generation complete.")

    audio_filepath = os.path.join(dirname, audio_filename)
    audio = WAVE(audio_filepath)
    audio_duration = int(audio.info.length)

    print(f"Duration in seconds: {audio_duration}")
    



main()