from PySide6.QtUiTools import QUiLoader

UI_FILE_PATH = 'ui\main_window.ui'


class MainWindow:
    def __init__(self):
        self.loader = QUiLoader()
        self.window = self.loader.load(UI_FILE_PATH)
        with open('style.qss', 'r') as file:
            self.window.setStyleSheet(file.read())
        self.window.show()
        self.window.setWindowTitle('Mini Text Editor')

        self.window.btn_set_plain_text.clicked.connect(self.set_plain_text)
        self.window.btn_set_html.clicked.connect(self.set_html)

    def set_plain_text(self):
        self.window.text_edit.setPlainText(
            '"And in the end the love you take is equal to the love you make."')

    def set_html(self):
        self.window.text_edit.setHtml('''
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
