from mangnify.utils import logging
from mangnify.utils.ui_utils import update_log_area_callback

logger = logging.getLogger(__name__)


def process_images(app) -> None:
    """
    Process the images.
    """

    logger.info("Processing images...")
    update_log_area_callback(app, "\nProcessing images...")
    logger.info("Images processed.")
    update_log_area_callback(app, "Images processed.")
