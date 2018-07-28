from PyQt5 import QtCore, QtWidgets, uic
import sys


class ToDoList(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi('forms/main_window.ui', self)


def execute_app():
    app = QtWidgets.QApplication(sys.argv)
    main_window = ToDoList()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    execute_app()
