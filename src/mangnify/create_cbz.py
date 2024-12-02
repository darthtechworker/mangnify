from mangnify.utils import logging
from mangnify.utils.ui import update_log_area_callback

logger = logging.getLogger(__name__)


def create_cbz(app) -> None:
    """
    Create the CBZ file.
    """

    logger.info("Creating CBZ file...")
    update_log_area_callback(app, "\nCreating CBZ file...")
    logger.info("CBZ file created.")
    update_log_area_callback(app, "CBZ file created.")
