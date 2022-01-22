import requests
import ctypes
import pathlib
import urllib.request
import time
import logging.config
import logging
import os
import sys
from pathlib import Path


# Constants
PROJECT_DIRECTORY = os.path.abspath(os.path.expanduser(os.path.dirname(sys.argv[0])))

API = "https://api.unsplash.com"
TOKEN = ""
TMP_IMAGE_PATH = pathlib.Path("C:/Users/Slava/Pictures/unsplash_images/tmp.jpg")
DICTLOGCONFIG = {
    "version": 1,
    "handlers": {
        "fileHandler": {
            "class": "logging.FileHandler",
            "formatter": "myFormatter",
            "filename": Path(f"{PROJECT_DIRECTORY}\\logs.log")
        }
    },
    "loggers": {
        "set_wallpaper.py": {
            "handlers": ["fileHandler"],
            "level": "INFO",
        }
    },
    "formatters": {
        "myFormatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    }
}
logging.config.dictConfig(DICTLOGCONFIG)

# Variables
random_image_method = "photos/random"
image_orientation = "orientation=landscape"
auth = f"client_id={TOKEN}"
logger = logging.getLogger("set_wallpaper.py")


# Functions
def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, str(image_path), 0x2)
    time.sleep(3)


def download_image(image_url):
    urllib.request.urlretrieve(image_url, TMP_IMAGE_PATH)


def delete_tmp_image(image_path):
    os.remove(image_path)


def main():
    # Calls
    logger.info("Sending get request...")
    try:
        response = requests.get(f"{API}/{random_image_method}/?{image_orientation}&{auth}")
        json_response = response.json()
    except Exception as e:
        logger.error(f"{e}\n")
        raise SystemExit(1)

    if response.status_code != 200:
        logger.error(f'Response status code - {response.status_code}: {json_response["errors"]}\n')
        raise SystemExit(1)
    else:
        logger.info(f'Response status code - {response.status_code}: OK')

    image_url = json_response["urls"]["raw"]
    logger.info("Downloading the background image...")
    try:
        download_image(image_url)
    except Exception as e:
        logger.error(f"Failed downloading the background image, {e}\n")
        raise SystemExit(1)

    logger.info("Image downloaded")
    logger.info("Setting wallpaper...")
    set_wallpaper(TMP_IMAGE_PATH)
    logger.info("Wallpaper has been set")
    delete_tmp_image(TMP_IMAGE_PATH)
    logger.info("TMP image has been deleted\n")


if __name__ == "__main__":
    main()
