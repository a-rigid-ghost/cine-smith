import os
from google_images_search import GoogleImagesSearch

from constants import GCS_DEVELOPER_KEY, GCS_CX

def fetch_image_from_prompt(query: str, dirname):
    gis = GoogleImagesSearch(GCS_DEVELOPER_KEY, GCS_CX)
    _search_params = {
        'q': query,
        'num': 2,
        'imgType': 'photo',
        'imgSize': 'large'
    }
    gis.search(search_params=_search_params, path_to_dir=os.path.join(dirname, "images"))