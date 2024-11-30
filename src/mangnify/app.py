import toga
from toga.style.pack import Pack, COLUMN
from .ui.main import init_ui


class Mangnify(toga.App):
    def startup(self):
        """
        App startup
        """

        self.input_directory = None

        self.main_window = toga.MainWindow(
            title=f"{self.formal_name} v{self.version}",
            size=(400, 400),
            resizable=False,
        )

        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        self.main_window.content = self.main_box

        init_ui(self)

        self.main_window.show()


def main():
    return Mangnify()