from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton
)
'''
When using __feature__ often with common IDEs, you may want to provide a feature-aware version of .pyi files to get a correct display. The simplest way to change them all in-place is the command:
# pyside6-genpyi all --feature snake_case true_property
'''
from __feature__ import snake_case, true_property


img_path = 'imgs/python_logo.png'


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.window_title = 'QLabel Image'

        img_label = QLabel()
        img_label.pixmap = QPixmap(img_path)

        layout = QVBoxLayout()
        layout.add_widget(img_label)

        self.set_layout(layout)
