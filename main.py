import os

from text_generator.dialogue_creator import get_dialogue
from text_generator.constants import OPENAI_API_KEY

from audio_generator.text_to_speech import convert_text_to_speech

# Login -> https://platform.openai.com/api-keys -> Generate Key -> Replace here
os.environ[OPENAI_API_KEY] = "<YOUR_API_KEY>"
IDEA_PROMPT = "Top 10 Places to visit in Schengen Area"
AUDIO_SPEED = 200

def main():
    dialogue = get_dialogue(idea_prompt=IDEA_PROMPT)
    filename = f"audio_file_{IDEA_PROMPT}.mp3"
    convert_text_to_speech(dialogue, AUDIO_SPEED, filename)

main()