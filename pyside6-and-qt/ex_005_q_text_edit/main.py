import sys

from PySide6.QtWidgets import QApplication

from widget import Widget


app = QApplication(sys.argv)

widget = Widget()
widget.show()

app.exec()
