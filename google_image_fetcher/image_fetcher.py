import os
from google_images_search import GoogleImagesSearch

from constants import GCS_DEVELOPER_KEY, GCS_CX, GENERATED_MEDIA_FOLDER, NUMBER_OF_IMAGES

def fetch_image_from_prompt(query: str, dirname):
    gis = GoogleImagesSearch(GCS_DEVELOPER_KEY, GCS_CX)
    _search_params = {
        'q': query,
        'num': NUMBER_OF_IMAGES,
        'imgType': 'photo',
        'imgSize': 'large'
    }
    gis.search(search_params=_search_params, path_to_dir=dirname)