import sys

from PyQt5.Qt import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen, qApp

from configs.Config import Config
from windows.MainWindow import ToDoList
from windows.SplashScreen import SplashScreen


def execute_app():
    app = QApplication(sys.argv)
    splash = SplashScreen()
    qApp.processEvents()
    main_window = ToDoList()
    main_window.load_data(splash)
    main_window.showMaximized()
    splash.finish(main_window)
    sys.exit(app.exec_())


if __name__ == '__main__':
    execute_app()
