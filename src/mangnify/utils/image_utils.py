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

    Args:
        image (numpy.ndarray): The input image.

    Returns:
        numpy.ndarray: The cropped image without empty margins.
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


def save_image(image_path: str, image: np.ndarray, jpg_quality: int) -> None:
    """
    Save the image.

    Parameters:
    image_path (str): The path to save the image.
    image (np.ndarray): The image to save.
    jpg_quality (int): The JPEG quality of the saved image.
    """

    cv2.imwrite(image_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])
