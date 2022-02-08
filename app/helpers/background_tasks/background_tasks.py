from pydantic import FilePath
import os


def clean_directory(image_path:FilePath):
    os.remove(image_path)
    return