import toga
from toga.style.pack import Pack, COLUMN
from .ui.main import build_ui

WIDTH = 400
HEIGHT = 400


class Mangnify(toga.App):
    def startup(self):
        """
        App startup
        """

        # Directory paths
        self.input_directory = None
        self.output_directory = None
        self.working_directory = None

        # Functionality flags
        self.is_processing_needed = None
        self.is_keep_images = None

        # Image options
        self.jpg_quality = None
        self.is_trim_images = None
        self.trim_limit = None
        self.add_margins = None
        self.is_rotate_spread = None

        # CBZ options
        self.is_cbz_needed = None

        # AZW3 options
        self.is_azw3_needed = None
        self.is_grayscale = None
        self.compression_level = None

        self.main_window = toga.MainWindow(
            title=f"{self.formal_name} v{self.version}",
            size=(WIDTH, HEIGHT),
            resizable=False,
        )

        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        self.main_window.content = self.main_box

        build_ui(self)

        self.main_window.show()


def main():
    return Mangnify()
