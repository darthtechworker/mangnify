import ctypes
import os
import platform
import re
import shutil
import subprocess
import unicodedata
import zipfile
from typing import List

from mangnify.utils import logging

logger = logging.getLogger(__name__)

hi_res_azw3_lib = None

if platform.system() == "Darwin":
    hi_res_azw3_lib = hi_res_azw3_lib = ctypes.CDLL(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../resources/hiresazw3.dylib")
        )
    )

hi_res_azw3_lib.CreateAZW3.argtypes = [
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_int,
    ctypes.c_int,
]

hi_res_azw3_lib.CreateAZW3.restype = ctypes.c_char_p

SUPPORTED_IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png"]


def cleanup(directory_path) -> None:
    """
    Cleanup the working directory.

    Parameters:
    directory_path (str): The path of the directory to cleanup
    """

    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)


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


def sanitize_title(title: str, max_length: int = 100) -> str:
    """
    Sanitizes a title for use as a filename.

    Parameters:
    title (str): The title to sanitize.

    Returns:
    str: A sanitized filename-safe title.
    """

    title = unicodedata.normalize("NFC", title)

    title = re.sub(r'[<>:"/\\|?*\n\r\t]', "_", title)

    title = "".join(char for char in title if char.isprintable())

    title = title.strip(" .")

    if len(title) > max_length:
        title = title[:max_length].rstrip(" .")

    reserved_names = {
        "CON",
        "PRN",
        "AUX",
        "NUL",
        "COM1",
        "COM2",
        "COM3",
        "COM4",
        "COM5",
        "COM6",
        "COM7",
        "COM8",
        "COM9",
        "LPT1",
        "LPT2",
        "LPT3",
        "LPT4",
        "LPT5",
        "LPT6",
        "LPT7",
        "LPT8",
        "LPT9",
    }
    if title.upper() in reserved_names:
        title += "_file"

    return title


def package_cbz(input_directory, output_directory, title) -> None:
    """
    Package images into a CBZ file.

    Parameters:
    input_directory (str): The path of the input directory.
    output_directory (str): The path of the output directory.
    """

    santized_title = sanitize_title(title)
    cbz_path = os.path.join(output_directory, f"{santized_title}.cbz")

    with zipfile.ZipFile(cbz_path, "w") as cbz_file:
        for image_name in os.listdir(input_directory):
            if image_name.lower().endswith(tuple(SUPPORTED_IMAGE_EXTENSIONS)):
                image_path = os.path.join(input_directory, image_name)
                cbz_file.write(image_path, arcname=image_name)

        comic_info_path = os.path.join(input_directory, "ComicInfo.xml")
        if os.path.exists(comic_info_path):
            cbz_file.write(comic_info_path, arcname="ComicInfo.xml")


def package_azw3(
    input_directory, output_directory, title, writer, is_manga, compression_level
) -> str:
    """
    Package images into a AZW3 file.

    Parameters:
    input_directory (str): The path of the input directory.
    output_directory (str): The path of the output directory.
    title (str): The title of the Comic/Manga.
    writer (str): The writer of the Comic/Manga.
    is_manga (bool): Whether the content is a manga.
    compression_level (int): The compression level of the images in the AZW3 file.

    Returns:
    str: The result of the operation.
    """
    input_directory_c = ctypes.c_char_p(str(input_directory).encode("utf-8"))
    output_directory_c = ctypes.c_char_p(str(output_directory).encode("utf-8"))
    title_c = ctypes.c_char_p(title.encode("utf-8"))
    writer_c = ctypes.c_char_p(writer.encode("utf-8"))
    is_manga_c = ctypes.c_int(is_manga)
    compression_level_c = ctypes.c_int(compression_level)

    # Call the CreateAZW3 function from the shared library
    result = hi_res_azw3_lib.CreateAZW3(
        input_directory_c,
        output_directory_c,
        title_c,
        writer_c,
        is_manga_c,
        compression_level_c,
    )

    result = result.decode("utf-8")
    logger.info(f"{result}")

    return result


def open_directory_in_ui(directory_path: str) -> None:
    """
    Open the directory in the file explorer.

    Parameters:
    directory_path (str): The path of the directory to open.
    """

    system = platform.system()

    if system == "Darwin":  # macOS
        subprocess.run(["open", directory_path], check=True)
    elif system == "Windows":  # Windows
        os.startfile(directory_path)
    elif system == "Linux":  # Linux
        subprocess.run(["xdg-open", directory_path], check=True)
    else:
        print(f"Unsupported operating system: {system}")
