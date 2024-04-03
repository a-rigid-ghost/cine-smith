import os

from text_generator.dialogue_creator import get_dialogue
from text_generator.constants import OPENAI_API_KEY

from audio_generator.text_to_speech import convert_text_to_speech

# Login -> https://platform.openai.com/api-keys -> Generate Key -> Replace here
os.environ[OPENAI_API_KEY] = "<ADD YOUR KEY>"
IDEA_PROMPT = "Top 10 Characters in Dragon Ball Z"
AUDIO_SPEED = 100

def main():
    dialogue = get_dialogue(idea_prompt=IDEA_PROMPT)
    convert_text_to_speech(dialogue, AUDIO_SPEED)

main()