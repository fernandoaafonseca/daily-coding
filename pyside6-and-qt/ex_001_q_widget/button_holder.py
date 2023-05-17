from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QPushButton


def button_clicked(data):
    print(f'You cliked the button! - {data}')


# def respond_to_slider(data):
#     print(f'The value is: {data}')


class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')
        button = QPushButton()
        button.setText('Press me')
        button.setCheckable(True)
        self.setCentralWidget(button)
        button.clicked.connect(button_clicked)

        # slider = QSlider(Qt.Horizontal)
        # slider.setMinimum(1)
        # slider.setMaximum(100)
        # slider.setValue(25)
        # slider.valueChanged.connect(respond_to_slider)