

from PySide6.QtWidgets import (
    QApplication,
    QWidget)
from PySide6.QtGui import QIcon

import pathlib
import sys

from __feature__ import snake_case
# from __feature__ import true_property


current_directory = str(pathlib.Path(__file__).parent.absolute())


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_style_constants()
        self.init_UI()

    def init_style_constants(self):
        self.WINDOW_ICON_PATH = current_directory + '/icon/qt.png'
        self.BACKGROUND_COLOR = 'lightblue'

    def init_UI(self):
        self.set_window_title('Qt Window Icon')
        self.set_geometry(200, 200, 400, 200)
        self.set_window_icon(QIcon(self.WINDOW_ICON_PATH))
        self.set_style_sheet(f'background-color: {self.BACKGROUND_COLOR}')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
