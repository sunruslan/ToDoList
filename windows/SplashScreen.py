from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from configs.Config import Config


class SplashScreen(QSplashScreen):
    def __init__(self):
        super(SplashScreen, self).__init__(QPixmap(Config.APP_LOADER))
        self.showMessage("Загрузка данных", Qt.AlignHCenter |
                           Qt.AlignVCenter | Qt.gray)
        self.show()
