from PySide6.QtWidgets import (QWidget,
                               QHBoxLayout,
                               QVBoxLayout,
                               QPushButton,
                               QTextEdit)


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QTextEdit')

        self.text_edit = QTextEdit()

        copy_button = QPushButton('Copy')
        copy_button.clicked.connect(self.text_edit.copy)

        cut_button = QPushButton('Cut')
        cut_button.clicked.connect(self.text_edit.cut)

        paste_button = QPushButton('Paste')
        paste_button.clicked.connect(self.text_edit.paste)

        undo_button = QPushButton('Undo')
        undo_button.clicked.connect(self.text_edit.undo)

        redo_button = QPushButton('Redo')
        redo_button.clicked.connect(self.text_edit.redo)

        set_plain_text_button = QPushButton('Set plain text')
        set_plain_text_button.clicked.connect(self.set_plain_text)

        set_html_button = QPushButton('Set HTML')
        set_html_button.clicked.connect(self.set_html)

        clear_button = QPushButton('Clear')
        clear_button.clicked.connect(self.text_edit.clear)

        h_layout = QHBoxLayout()
        h_layout.addWidget(copy_button)
        h_layout.addWidget(cut_button)
        h_layout.addWidget(paste_button)
        h_layout.addWidget(undo_button)
        h_layout.addWidget(redo_button)
        h_layout.addWidget(set_plain_text_button)
        h_layout.addWidget(set_html_button)
        h_layout.addWidget(clear_button)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.text_edit)

        self.setLayout(v_layout)

    def set_plain_text(self):
        self.text_edit.setPlainText(
            '"And in the end the love you take is equal to the love you make."')

    def set_html(self):
        self.text_edit.setHtml('''
<h1>The Beatles</h1>
<h2>The End</h2>
<br>
<p>"Oh yeah, all right</p>
<p>Are you going to be in my dreams</p>
<p>Tonight?</p>
<br>
<p>And in the end</p>
<p>The love you take</p>
<p>Is equal to the love you make"</p>
''')
