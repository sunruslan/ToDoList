import time
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from configs.Config import Config
from windows.AddTaskWindow import AddTaskWindow


class ToDoList(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.main_form = MainForm(self)
        self.setCentralWidget(self.main_form)
        self.set_ui()
        self.connecting()

    def set_ui(self):
        parts = (Config.APP_NAME, Config.APP_VERSION)
        self.setWindowTitle(' '.join(parts))
        self.setWindowOpacity(0.95)
        self.setWindowIcon(QIcon(Config.APP_ICON))
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor("#FFFEBF"))
        self.setPalette(p)
        self.tb = self.addToolBar("ToolBar")
        p = self.tb.palette()
        p.setColor(self.tb.backgroundRole(), QColor("#FFFCA8"))
        self.tb.setPalette(p)
        self.tb.setMovable(False)
        self.add = QAction(QIcon("images/icons/add.png"), "add", self)
        self.tb.addAction(self.add)
        self.delete = QAction(QIcon("images/icons/delete.png"), "delete", self)
        self.tb.addAction(self.delete)
        self.search = QAction(QIcon("images/icons/search.png"), "search", self)
        self.tb.addAction(self.search)
        self.history = QAction(QIcon("images/icons/history.png"), "history", self)
        self.tb.addAction(self.history)
        self.update = QAction(QIcon("images/icons/update.png"), "update", self)
        self.tb.addAction(self.update)
        self.trash = QAction(QIcon("images/icons/trash.png"), "trash", self)
        self.tb.addAction(self.trash)
        self.send = QAction(QIcon("images/icons/send.png"), "send", self)
        self.tb.addAction(self.send)
        self.share = QAction(QIcon("images/icons/share.png"), "share", self)
        self.tb.addAction(self.share)
        self.exit = QAction(QIcon("images/icons/exit.png"), "exit", self)
        self.tb.addAction(self.exit)

    def connecting(self):
        self.add.triggered.connect(self.add_task)
        self.exit.triggered.connect(self.close)

    def add_task(self):
        window = AddTaskWindow(self)
        window.exec_()

    def closeEvent(self, event: QCloseEvent):
        event.accept()

    @staticmethod
    def load_data(sp):
        for i in range(1, 11):
            if i % 2:
                time.sleep(0.1)
            sp.showMessage("Загрузка данных... {0}".format(i*10), Qt.AlignHCenter |
                       Qt.AlignVCenter | Qt.gray)
            qApp.processEvents()


class MainForm(QWidget):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.layout = QGridLayout()
        self.label1 = QLabel("Срочные")
        self.label1.setAlignment(Qt.AlignHCenter)
        self.list1 = QListWidget()
        self.list1.setStyleSheet("QListWidget::item { border-style: solid;"
                                                     "border-width: 0px 0px 1px 0px;"
                                                     "border-color: red; }")
        p = self.list1.palette()
        p.setColor(self.list1.backgroundRole(), Qt.red)
        self.list1.setPalette(p)
        self.label2 = QLabel("Важные")
        self.label2.setAlignment(Qt.AlignHCenter)
        self.list2 = QListWidget()
        p = self.list2.palette()
        p.setColor(self.list2.backgroundRole(), Qt.yellow)
        self.list2.setPalette(p)
        self.label3 = QLabel("Не срочные")
        self.label3.setAlignment(Qt.AlignHCenter)
        self.list3 = QListWidget()
        p = self.list3.palette()
        p.setColor(self.list3.backgroundRole(), Qt.green)
        self.list3.setPalette(p)
        self.label4 = QLabel("Сделанные")
        self.label4.setAlignment(Qt.AlignHCenter)
        self.list4 = QListWidget()
        p = self.list4.palette()
        p.setColor(self.list1.backgroundRole(), Qt.blue)
        self.list4.setPalette(p)
        self.layout.addWidget(self.label1, 0, 0)
        self.layout.addWidget(self.label2, 0, 1)
        self.layout.addWidget(self.label3, 0, 2)
        self.layout.addWidget(self.label4, 0, 3)
        self.layout.addWidget(self.list1, 1, 0)
        self.layout.addWidget(self.list2, 1, 1)
        self.layout.addWidget(self.list3, 1, 2)
        self.layout.addWidget(self.list4, 1, 3)
        self.setLayout(self.layout)

