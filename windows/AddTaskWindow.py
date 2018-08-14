import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class AddTaskWindow(QDialog):
    def __init__(self, parent=None):
        super(AddTaskWindow, self).__init__(parent)
        self.set_ui()

    def set_ui(self):
        layout = QFormLayout()
        name = QLineEdit()
        name.setMaxLength(20)
        name.setAlignment(Qt.AlignHCenter)
        description = QLineEdit()
        description.setMaxLength(1024)
        creator = QLineEdit()
        executor = QLineEdit()
        layout.addRow('Название', name)
        layout.addRow('Описание', description)
        layout.addRow('Создатель', creator)
        layout.addRow('Исполнитель', executor)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AddTaskWindow()
    window.show()
    sys.exit(app.exec_())