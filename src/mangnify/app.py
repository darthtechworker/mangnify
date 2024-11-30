import toga


class Mangnify(toga.App):
    def startup(self):
        """
        App startup
        """
        main_box = toga.Box()

        self.main_window = toga.MainWindow(
            title=f"{self.formal_name} v{self.version}",
            size=(400, 400),
            resizeable=False,
        )
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return Mangnify()
