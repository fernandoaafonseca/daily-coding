from PySide6.QtWidgets import QPushButton, QSlider, QWidget, QVBoxLayout
from PySide6.QtCore import Qt


class WidgetLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')

        button = QPushButton()
        button.setText('Press me')
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)

        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(1)
        slider.setMaximum(100)
        slider.setValue(25)
        slider.valueChanged.connect(self.respond_to_slider)

        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(slider)
        self.setLayout(layout)


    def button_clicked(data):
        print(f'You cliked the button! - {data}')


    def respond_to_slider(data):
        print(f'The value is: {data}')