# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 719)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"background-color: #32383D;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btns_container = QFrame(self.centralwidget)
        self.btns_container.setObjectName(u"btns_container")
        self.btns_container.setEnabled(True)
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.btns_container.setFont(font)
        self.btns_container.setStyleSheet(u"QFrame {\n"
"}\n"
"\n"
"QPushButton {\n"
"color: #A1B4C4;\n"
"border-radius: 5px;\n"
"\n"
"background: qlineargradient(x1:0, y1:0, x1:0, y2:1,\n"
"                                  stop:0 #dbddde, stop:0.05 #6f767c, stop:1  #4C555C);\n"
"height: 25px;\n"
"font: 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qlineargradient(x1:0, y1:0, x1:0, y2:1,\n"
"                                  stop:0 #e8f9f7, stop:0.1 #a3e8e1, stop:0.9  #1BC6B4, stop:1 #083b36);\n"
"color: #034159;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"height: 40px;\n"
"font: 750 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"")
        self.btns_container.setFrameShape(QFrame.StyledPanel)
        self.btns_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.btns_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_copy = QPushButton(self.btns_container)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.btn_copy.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_copy)

        self.btn_cut = QPushButton(self.btns_container)
        self.btn_cut.setObjectName(u"btn_cut")
        self.btn_cut.setMinimumSize(QSize(0, 0))
        self.btn_cut.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_cut)

        self.btn_past = QPushButton(self.btns_container)
        self.btn_past.setObjectName(u"btn_past")
        self.btn_past.setMinimumSize(QSize(0, 0))
        self.btn_past.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_past)

        self.btn_undo = QPushButton(self.btns_container)
        self.btn_undo.setObjectName(u"btn_undo")
        self.btn_undo.setMinimumSize(QSize(0, 0))
        self.btn_undo.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_undo)

        self.btn_redo = QPushButton(self.btns_container)
        self.btn_redo.setObjectName(u"btn_redo")
        self.btn_redo.setMinimumSize(QSize(0, 0))
        self.btn_redo.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_redo)

        self.btn_set_plain_text = QPushButton(self.btns_container)
        self.btn_set_plain_text.setObjectName(u"btn_set_plain_text")
        self.btn_set_plain_text.setMinimumSize(QSize(0, 0))
        self.btn_set_plain_text.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_set_plain_text)

        self.btn_set_html = QPushButton(self.btns_container)
        self.btn_set_html.setObjectName(u"btn_set_html")
        self.btn_set_html.setMinimumSize(QSize(0, 0))
        self.btn_set_html.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_set_html)

        self.btn_clear = QPushButton(self.btns_container)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(0, 0))
        self.btn_clear.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_clear)

        self.btn_copy.raise_()
        self.btn_undo.raise_()
        self.btn_past.raise_()
        self.btn_set_plain_text.raise_()
        self.btn_cut.raise_()
        self.btn_set_html.raise_()
        self.btn_redo.raise_()
        self.btn_clear.raise_()

        self.verticalLayout.addWidget(self.btns_container)

        self.text_container = QFrame(self.centralwidget)
        self.text_container.setObjectName(u"text_container")
        font2 = QFont()
        font2.setPointSize(8)
        self.text_container.setFont(font2)
        self.text_container.setStyleSheet(u"QTextEdit {\n"
"background-color: #202529;\n"
"color: #A1B4C4;\n"
"selection-background-color: #A1B4C4;\n"
"selection-color: #202529;\n"
"}")
        self.text_container.setFrameShape(QFrame.StyledPanel)
        self.text_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.text_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.text_edit = QTextEdit(self.text_container)
        self.text_edit.setObjectName(u"text_edit")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        self.text_edit.setFont(font3)

        self.verticalLayout_2.addWidget(self.text_edit)


        self.verticalLayout.addWidget(self.text_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_copy.clicked.connect(self.text_edit.copy)
        self.btn_cut.clicked.connect(self.text_edit.cut)
        self.btn_past.clicked.connect(self.text_edit.paste)
        self.btn_undo.clicked.connect(self.text_edit.undo)
        self.btn_redo.clicked.connect(self.text_edit.redo)
        self.btn_clear.clicked.connect(self.text_edit.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.btn_cut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
        self.btn_past.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.btn_undo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.btn_redo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.btn_set_plain_text.setText(QCoreApplication.translate("MainWindow", u"Set plain text", None))
        self.btn_set_html.setText(QCoreApplication.translate("MainWindow", u"Set HTML", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi

