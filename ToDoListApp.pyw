import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, qApp

from windows.MainWindow import ToDoList
from windows.SplashScreen import SplashScreen
from log.Logger import Logger


def execute_app():
    QtCore.qInstallMessageHandler(Logger.instance())
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
