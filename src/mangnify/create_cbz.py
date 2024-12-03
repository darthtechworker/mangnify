from mangnify.utils import logging
from mangnify.utils.comic_info import write_comic_info
from mangnify.utils.file import copy_images, create_directory, package_cbz
from mangnify.utils.ui import update_log_area_callback

logger = logging.getLogger(__name__)


def create_cbz(app) -> None:
    """
    Create the CBZ file.
    """

    logger.info("Creating CBZ file...")
    update_log_area_callback(app, "\nCreating CBZ file...")

    try:
        create_directory(app.output_directory)
        create_directory(app.working_directory)

        if not app.is_processing_needed:
            copy_images(app.input_directory, app.working_directory)

        write_comic_info(app)

        package_cbz(app.working_directory, app.output_directory, app.title_input.value)

    except Exception as e:
        logger.exception(e)
        raise e

    logger.info("CBZ file created.")
    update_log_area_callback(app, "CBZ file created.")
