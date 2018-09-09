from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class InformationWindow(QWidget):
    def __init__(self, title, msg, parent=None):
        super(InformationWindow, self).__init__(parent)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(title)
        msgBox.setInformativeText(msg)
        msgBox.addButton(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)
        desktop = QApplication.desktop()
        x = (desktop.width() - self.frameSize().width()) // 2
        y = (desktop.height() - self.frameSize().height()) // 2
        self.move(x, y)
        msgBox.exec_()
