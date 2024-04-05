import os

from text_generator.dialogue_creator import get_dialogue
from constants import OPENAI_API_KEY
from google_image_fetcher.image_fetcher import fetch_image_from_prompt
from video_synthesizer.images_to_video import images_to_video

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

    dialogue = "Cats are pet animals. They are fat and are nasty bitches. I like them from afar. I do not want to mess with them."
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
    
    """
    For actual google search of images
    """
    # print("Google images from prompt")
    # fetch_image_from_prompt("high quality cats", dirname)

    image_filepath = os.path.join(dirname, "images")
    print(image_filepath)
    images_to_video(image_filepath)
    

main()