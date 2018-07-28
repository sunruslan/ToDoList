import time

from PyQt5 import QtCore, QtWidgets, QtGui
import sys
import forms.main_window


class AddTaskThread(QtCore.QThread):
    def run(self):
        pass


class TrashThread(QtCore.QThread):
    def run(self):
        pass


class ToDoList(QtWidgets.QMainWindow, forms.main_window.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.add_button.clicked.connect(self.on_add_button_clicked)
        self.setWindowFlags(QtCore.Qt.Window |
                                   QtCore.Qt.FramelessWindowHint |
                                   QtCore.Qt.WindowTitleHint)
        

    def on_add_button_clicked(self):
        self.add_button.setDisabled(True)
        thread = AddTaskThread()
        thread.start()
        thread.finished.connect(self.on_add_finished)

    def on_add_finished(self):
        self.add_button.setDisabled(False)

    def on_trash_button_clicked(self):
        pass

    @staticmethod
    def load_data(sp):
        for i in range(1, 11):
            if i % 2:
                time.sleep(0.5)
            sp.showMessage("Загрузка данных... {0}".format(i*10), QtCore.Qt.AlignHCenter |
                       QtCore.Qt.AlignBottom | QtCore.Qt.gray)
            QtWidgets.qApp.processEvents()

    def closeEvent(self, event):
        event.accept()


def execute_app():
    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap('logo.png'))
    splash.showMessage("Загрузка данных", QtCore.Qt.AlignHCenter |
                       QtCore.Qt.AlignBottom | QtCore.Qt.gray)
    splash.show()
    QtWidgets.qApp.processEvents()
    main_window = ToDoList()
    main_window.load_data(splash)
    main_window.showFullScreen()
    splash.finish(main_window)
    sys.exit(app.exec_())


if __name__ == '__main__':
    execute_app()
