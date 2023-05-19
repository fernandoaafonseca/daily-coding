import sys


from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice

from main_window import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()

    sys.exit(app.exec())
