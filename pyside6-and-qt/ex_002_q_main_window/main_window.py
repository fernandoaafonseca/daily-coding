from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QStatusBar, QPushButton


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle('Main Window')

        # Menus
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu('&File')
        # a letra que segue o "&" será o atalho (ex.: Alt+f)
        quit_action = file_menu.addAction('Quit')
        quit_action.triggered.connect(self.quit_app)
        quit_action.setStatusTip('Exit the app')

        edit_menu = menu_bar.addMenu('&Edit')
        edit_menu.addAction('Copy')
        edit_menu.addAction('Cut')
        edit_menu.addAction('Paste')
        
        help_menu = menu_bar.addMenu('&Help')

        
        #Toolbars
        toolbar = QToolBar('Main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar.addAction(quit_action)

        action1 = QAction('Some action', self)
        action1.setStatusTip('Status message')
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon('start.png'), 'Other action', self)
        action2.setStatusTip('Status message')
        action2.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton('Click here'))


        #Status bar
        self.setStatusBar(QStatusBar(self))


        button1 = QPushButton('Button 1')
        button1.clicked.connect(self.button_clicked)
        self.setCentralWidget(button1)


    def quit_app(self):
        self.app.quit()


    def toolbar_button_click(self):
        self.statusBar().showMessage('Message from my app', 3000)

    
    def button_clicked(self):
        self.statusBar().showMessage('You clicked the button!', 3000)