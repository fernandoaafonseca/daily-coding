from PySide6.QtWidgets import QApplication
from widget_layout import WidgetLayout
import sys


app = QApplication(sys.argv)

window = WidgetLayout()
window.show()

app.exec()