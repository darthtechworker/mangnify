from mangnify.utils import logging
from mangnify.utils.ui_utils import update_log_area_callback

logger = logging.getLogger(__name__)


def create_azw3(app) -> None:
    """
    Create the AZW3 file.
    """

    logger.info("Creating AZW3 file...")
    update_log_area_callback(app, "\nCreating AZW3 file...")
    logger.info("AZW3 file created.")
    update_log_area_callback(app, "AZW3 file created.")
