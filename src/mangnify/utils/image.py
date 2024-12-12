import cv2
import numpy as np
import pyopencl as cl
from realcugan_ncnn_py import Realcugan

from mangnify.utils import logging
from mangnify.utils.ui import update_log_area_callback

logger = logging.getLogger(__name__)


def load_image(image_path: str, is_grayscale: bool = False) -> np.ndarray:
    """
    Load the image.

    Parameters:
    image_path (str): The path of the image to load.
    is_grayscale (bool): Whether to load the image as grayscale.

    Returns:
    np.ndarray: The loaded image.
    """

    if is_grayscale:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    else:
        image = cv2.imread(image_path)

    return image


def trim_margins(image: np.ndarray, trim_limit: int) -> np.ndarray:
    """
    Trims the empty margins from the image.

    Parameters:
    image (np.ndarray): The image to trim.
    trim_limit (int): The limit in percentage of width and height to trim.

    Returns:
    np.ndarray: The trimmed image.
    """

    trim_limit = trim_limit / 100.0

    white_mask = cv2.inRange(image, (240, 240, 240), (255, 255, 255))
    black_mask = cv2.inRange(image, (0, 0, 0), (5, 5, 5))

    combined_mask = cv2.bitwise_or(white_mask, black_mask)

    content_mask = cv2.bitwise_not(combined_mask)
    coords = cv2.findNonZero(content_mask)

    if coords is not None:
        x, y, w, h = cv2.boundingRect(coords)

        height, width = image.shape[:2]
        max_trim_x = int(width * trim_limit)
        max_trim_y = int(height * trim_limit)

        x_start = min(x, max_trim_x)
        x_end = max(x + w, width - max_trim_x)
        y_start = min(y, max_trim_y)
        y_end = max(y + h, height - max_trim_y)

        trimmed = image[y_start:y_end, x_start:x_end]
        return trimmed
    else:
        return image


def add_margins(image: np.ndarray, margin: int) -> np.ndarray:
    """
    Add margin to the image.

    Parameters:
    image (np.ndarray): The image to add margin.
    margin (int): The margin in percentage of longer edge.

    Returns:
    np.ndarray: The image with margin.
    """

    height, width = image.shape[:2]
    longer_edge = max(height, width)
    margin_size = int(longer_edge * margin / 100)

    top = bottom = left = right = margin_size

    if height > width:
        left = right = margin_size
    else:
        top = bottom = margin_size

    color = [255, 255, 255]
    bordered = cv2.copyMakeBorder(
        image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color
    )

    return bordered


def rotate_spread(image: np.ndarray) -> np.ndarray:
    """
    Rotate the image 90 degrees if it is a spread.

    Parameters:
    image (np.ndarray): The image to rotate.

    Returns:
    np.ndarray: The rotated image.
    """

    height, width = image.shape[:2]

    if width > height:
        rotated = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

        return rotated
    else:
        return image


def save_image(image_path: str, image: np.ndarray, jpg_quality: int) -> None:
    """
    Save the image.

    Parameters:
    image_path (str): The path to save the image.
    image (np.ndarray): The image to save.
    jpg_quality (int): The JPEG quality of the saved image.
    """

    cv2.imwrite(image_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])


def resize_image(image: np.ndarray, max_height: int, max_width: int) -> np.ndarray:
    """
    Resize the image while maintaining the aspect ratio.

    Parameters:
    image (np.ndarray): The image to resize.
    max_height (int): The maximum height of the resized image.
    max_width (int): The maximum width of the resized image.

    Returns:
    np.ndarray: The resized image.
    """

    height, width = image.shape[:2]
    aspect_ratio = width / height

    if width > height:
        new_width = min(width, max_width)
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = min(height, max_height)
        new_width = int(new_height * aspect_ratio)

    resized = cv2.resize(
        image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4
    )

    return resized


def init_realcugan(app, scale_factor: int) -> Realcugan:
    """
    Initialize the Realcugan model.
    Choose GPU if available, otherwise use CPU.
    If multiple GPUs are available, choose the one with the most memory.

    Parameters:
    app (App): The application object.
    scale_factor (int): The factor to upscale the image by.

    Returns:
    Realcugan: The Realcugan model.
    """

    platforms = cl.get_platforms()
    gpus = [
        device
        for platform in platforms
        for device in platform.get_devices(device_type=cl.device_type.GPU)
    ]
    if gpus:
        selected_device = max(gpus, key=lambda gpu: gpu.global_mem_size)
        update_log_area_callback(
            app,
            f"Using GPU: {selected_device.name}",
        )
    else:
        selected_device = None
        update_log_area_callback(
            app, "No GPU found, using CPU instead.\nProcessing will be slow..."
        )

    realcugan = Realcugan(
        gpuid=gpus.index(selected_device) if selected_device else -1,
        scale=scale_factor,
    )

    return realcugan


def upscale_image(image: np.ndarray, realcugan: Realcugan) -> np.ndarray:
    """
    Upscale the image using Realcugan.

    Parameters:
    image (np.ndarray): The image to upscale.
    realcugan (Realcugan): The Realcugan model.

    Returns:
    np.ndarray: The upscaled image.
    """

    upscaled = realcugan.process_cv2(image)

    return upscaled
