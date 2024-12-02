import cv2
import numpy as np


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


def save_image(image_path: str, image: np.ndarray, jpg_quality: int) -> None:
    """
    Save the image.

    Parameters:
    image_path (str): The path to save the image.
    image (np.ndarray): The image to save.
    jpg_quality (int): The JPEG quality of the saved image.
    """

    cv2.imwrite(image_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])
