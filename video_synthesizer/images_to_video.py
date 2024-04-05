import os
from PIL import Image
from moviepy.editor import *

def images_to_video(image_folder_path):
    resized_folder_path = make_resized_image_folder()
    resize_images(image_folder_path,resized_folder_path)
    resized_images = [os.path.join(resized_folder_path, img) for img in os.listdir(resized_folder_path)]
    video_folder = make_video_folder()
    generate_video(resized_images, video_folder)

def make_resized_image_folder():
    resized_dir_path = os.path.join(os.getcwd(), "resized_images")
    if not os.path.exists(resized_dir_path):
        os.makedirs(resized_dir_path)
    return resized_dir_path

def make_video_folder():
    video_dir_path = os.path.join(os.getcwd(), "videos")
    if not os.path.exists(video_dir_path):
        os.makedirs(video_dir_path)
    return video_dir_path

def resize_images(image_folder_path, resized_image_folder_path):
    path = image_folder_path
    dirs = os.listdir(path)

    for item in dirs:
        print("Starting image resize")
        im = Image.open(os.path.join(path, item))
        imResize = im.resize((800,800), Image.Resampling.LANCZOS)
        imResize = imResize.convert('RGB')
        imResize.save(os.path.join(resized_image_folder_path, item), "JPEG")

def generate_video(resized_images, video_folder):
    print(resized_images)
    clips = [ImageClip(m).set_duration(4)for m in resized_images]

    concat_clip = concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile(os.path.join(video_folder, "video.mp4"), fps=24)
