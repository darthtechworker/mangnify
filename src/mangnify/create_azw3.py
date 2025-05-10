from mangnify.utils import logging
from mangnify.utils.file import (
    copy_images,
    create_directory,
    package_azw3,
)
from mangnify.utils.ui import update_log_area_callback

logger = logging.getLogger(__name__)


def create_azw3(app) -> None:
    """
    Create the AZW3 file.
    """

    logger.info("Creating AZW3 file...")
    update_log_area_callback(app, "\nCreating AZW3 file...")

    try:
        create_directory(app.output_directory)
        create_directory(app.working_directory)

        if not app.is_processing_needed:
            copy_images(app.input_directory, app.working_directory)

        result = package_azw3(
            app.working_directory,
            app.output_directory,
            app.title,
            app.writer,
            app.is_manga,
            100,
        )

        update_log_area_callback(app, f"{result}")

    except Exception as e:
        logger.exception(e)
        raise e
