import os
import shutil
from typing import List

SUPPORTED_IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png"]


def create_directory(directory_path: str) -> None:
    """
    Create a directory if it does not already exist.

    Parameters:
    directory_path (str): The path of the directory to create.
    """

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def get_supported_images(directory_path) -> List[str]:
    """
    Get the supported images.

    Parameters:
    directory_path (str): The path of the directory containing the images.

    Returns:
    List[str]: The sorted names of the supported images.
    """

    image_names = []
    for image_name in os.listdir(directory_path):
        if image_name.lower().endswith(tuple(SUPPORTED_IMAGE_EXTENSIONS)):
            image_names.append(image_name)

    image_names.sort()

    return image_names


def copy_images(input_directory, output_directory) -> None:
    """
    Copy images from input directory to output directory.

    Parameters:
    input_directory (str): The path of the input directory.
    output_directory (str): The path of the output directory.
    """

    for image_name in os.listdir(input_directory):
        if image_name.lower().endswith(tuple(SUPPORTED_IMAGE_EXTENSIONS)):
            image_path = os.path.join(input_directory, image_name)
            output_path = os.path.join(output_directory, image_name)
            shutil.copy(image_path, output_path)
