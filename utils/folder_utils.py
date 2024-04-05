import os

def create_directory(parent_path, folder_name):
    dir_path = os.path.join(parent_path, folder_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path