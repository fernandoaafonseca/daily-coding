from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QLabel and QLineEdit')

        label = QLabel('Full name:')
        self.line_edit = QLineEdit()
        self.line_edit.editingFinished.connect(self.button_clicked)
        self.line_edit.selectionChanged.connect(self.selection_changed)

        button = QPushButton('Send')
        button.clicked.connect(self.button_clicked)

        self.text_holder_label = QLabel('I am here')
        self.text_holder_label2 = QLabel('Selection: ')

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)
        v_layout.addWidget(self.text_holder_label2)

        self.setLayout(v_layout)
    

    def button_clicked(self):
        print(f'Full name: {self.line_edit.text()}')
        self.text_holder_label.setText(f'{self.line_edit.text()}')

    
    def selection_changed(self):
        self.text_holder_label2.setText(f'Selection: {self.line_edit.selectedText()}')