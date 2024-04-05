import os
from PIL import Image
from moviepy.editor import *
from constants import IMAGE_SIZE, FPS, NUMBER_OF_IMAGES
from utils.folder_utils import create_directory

def images_to_video(image_folder_path, video_duration, media_dirname):
    resized_folder_path = create_directory(media_dirname, "resized_images")
    resize_images(image_folder_path,resized_folder_path)
    resized_images = [os.path.join(resized_folder_path, img) for img in os.listdir(resized_folder_path)]
    video_folder = create_directory(media_dirname, "videos")
    generate_video(resized_images, video_folder, video_duration)

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
    clips = [ImageClip(m).set_duration(video_duration/NUMBER_OF_IMAGES)for m in resized_images]

    concat_clip = concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile(os.path.join(video_folder, "video.mp4"), fps=FPS)
