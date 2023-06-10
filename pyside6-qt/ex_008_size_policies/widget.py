from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QSizePolicy
)
from __feature__ import snake_case


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.window_title = 'Size policies and stretches'

        label = QLabel('Text:')
        label.set_size_policy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        line_edit = QLineEdit()
        line_edit.set_size_policy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        button_1 = QPushButton('Button 1')
        button_2 = QPushButton('Button 2')
        button_3 = QPushButton('Button 3')

        h_layout_1 = QHBoxLayout()
        h_layout_1.add_widget(label)
        h_layout_1.add_widget(line_edit)

        h_layout_2 = QHBoxLayout()
        h_layout_2.add_widget(button_1, 2)
        h_layout_2.add_widget(button_2, 1)
        h_layout_2.add_widget(button_3, 1)

        v_layout = QVBoxLayout()
        v_layout.add_layout(h_layout_1)
        v_layout.add_layout(h_layout_2)

        self.set_layout(v_layout)
