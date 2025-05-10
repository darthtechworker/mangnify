import threading

import toga
from toga.style.pack import COLUMN, Pack

from mangnify.utils import logging

from .ui.main import build_ui

WIDTH = 360
HEIGHT = 400

logger = logging.getLogger(__name__)


class Mangnify(toga.App):
    def startup(self):
        """
        App startup
        """

        logger.info("Starting up the app...")

        # Directory paths
        self.input_directory = None
        self.output_directory = None
        self.working_directory = None

        # Functionality flags
        self.is_processing_needed = None
        self.is_keep_images = None

        # Image options
        self.jpg_quality = None
        self.is_trim_margins = None
        self.trim_limit = None
        self.add_margins = None
        self.is_rotate_spread = None
        self.scale_factor = None

        # Comic Info options
        self.title = None
        self.series = None
        self.volume = None
        self.writer = None
        self.is_manga = None

        # CBZ options
        self.is_cbz_needed = None

        # AZW3 options
        self.is_azw3_needed = None

        # Output options
        self.is_grayscale = None
        self.compression_level = None
        self.is_resize = None
        self.device_height = None
        self.device_width = None

        # Threading
        self.abort_event = threading.Event()

        self.main_window = toga.MainWindow(
            title=f"{self.formal_name} v{self.version}",
            size=(WIDTH, HEIGHT),
            resizable=False,
        )

        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        self.main_window.content = self.main_box

        build_ui(self)

        self.main_window.show()

        logger.info("App started.")

    def resize_window(self):
        """
        Resize the main window.
        """

        self.main_window.size = (WIDTH, HEIGHT)


def main():
    return Mangnify()
