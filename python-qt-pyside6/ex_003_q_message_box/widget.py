from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QMessageBox')

        button_hard = QPushButton('Hard')
        button_hard.clicked.connect(self.button_clicked_hard)

        button_critical = QPushButton('Critical')
        button_critical.clicked.connect(self.button_clicked_critical)

        button_question = QPushButton('Question')
        button_question.clicked.connect(self.button_clicked_question)

        button_information = QPushButton('Information')
        button_information.clicked.connect(self.button_clicked_information)

        button_warning = QPushButton('Warning')
        button_warning.clicked.connect(self.button_clicked_warning)

        button_about = QPushButton('About')
        button_about.clicked.connect(self.button_clicked_about)


        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        self.setLayout(layout)


    def button_clicked_hard(self):
        message = QMessageBox()
        message.setMaximumSize(700, 200)
        message.setWindowTitle('Hard')
        message.setText('Something happened!')
        message.setInformativeText('Do you want to do something about it?')
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print('MYou clicked Ok')
        else:
            print('MYou clicked Cancel')


    def button_clicked_critical(self):
        ret = QMessageBox.critical(self, 'Message title', 'Critical message!', QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print('You clicked Ok')
        else:
            print('You clicked Cancel')


    def button_clicked_question(self):
        ret = QMessageBox.question(self, 'Message title', 'Asking a question?', QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.Yes:
            print('MYou clicked Ok')
        else:
            print('MYou clicked Cancel')


    def button_clicked_information(self):
        pass


    def button_clicked_warning(self):
        pass


    def button_clicked_about(self):
        ret = QMessageBox.about(self, 'Message title', 'Some about message')