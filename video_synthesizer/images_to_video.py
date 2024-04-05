import os
from PIL import Image
from moviepy.editor import *
from constants import IMAGE_SIZE, FPS, NUMBER_OF_IMAGES
from utils.folder_utils import create_directory

def images_to_video(image_folder_path, video_duration, media_dirname):
    resized_folder_path = create_directory(media_dirname, "resized_images")
    video_folder = create_directory(media_dirname, "videos")
    audio_folder = os.path.join(media_dirname, "audios")
    resize_images(image_folder_path,resized_folder_path)
    resized_images = [os.path.join(resized_folder_path, img) for img in os.listdir(resized_folder_path)]
    generate_video(resized_images, video_folder, video_duration)
    clip_audio_with_video(video_folder,audio_folder)

def resize_images(image_folder_path, resized_image_folder_path):
    path = image_folder_path
    dirs = os.listdir(path)

    for item in dirs:
        print("Starting image resize")
        im = Image.open(os.path.join(path, item))
        imResize = im.resize((IMAGE_SIZE,IMAGE_SIZE), Image.Resampling.LANCZOS)
        imResize = imResize.convert('RGB')
        imResize.save(os.path.join(resized_image_folder_path, item), "JPEG")

def generate_video(resized_images, video_folder, video_duration):
    clip_duration = video_duration/NUMBER_OF_IMAGES
    print(clip_duration)
    clips = [ImageClip(m).set_duration(video_duration/NUMBER_OF_IMAGES)for m in resized_images]

    concat_clip = concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile(os.path.join(video_folder, "video.mp4"), fps=FPS)

def clip_audio_with_video(video_folder, audio_folder):
    video_file_path = os.path.join(video_folder, "video.mp4")
    audio_file_path = os.path.join(audio_folder, "audio_file.mp3")
    final_video_file_path = os.path.join(video_folder, "final_video.mp4")

    videoclip = VideoFileClip(video_file_path)
    audioclip = AudioFileClip(audio_file_path)

    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(final_video_file_path, fps=FPS)
