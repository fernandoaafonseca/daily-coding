from PySide6.QtWidgets import (QWidget,
                               QHBoxLayout,
                               QVBoxLayout,
                               QPushButton,
                               QTextEdit)


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QTextEdit')
