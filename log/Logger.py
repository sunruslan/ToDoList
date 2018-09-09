import logging
from sys import stderr

from PyQt5 import QtCore

from configs.Config import Config
from windows.InformationWindow import InformationWindow


class Logger(object):
    __instance = None

    @staticmethod
    def inst():
        if Logger.__instance is None:
            Logger.__instance = Logger()
        return Logger.__instance

    def __init__(self):
        self.logger = logging.getLogger('ToDoListLogger')
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(Config.LOG_FILE)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s\n %(message)s')
        fh.setFormatter(formatter)
        ch = logging.StreamHandler(stderr)
        ch.setFormatter(formatter)
        ch.setLevel(logging.DEBUG)
        msg_fmt = logging.Formatter('%(levelname)s\n %(message)s')
        wh = WindowHandler()
        wh.setFormatter(msg_fmt)
        wh.setLevel(logging.WARNING)
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)
        self.logger.addHandler(wh)

    def __call__(self, mode, context, message):
        msg = 'line: {0}, function: {1}, file: {2}\n {3}'\
                  .format(context.line, context.function, context.file, message)
        if mode == QtCore.QtInfoMsg:
            self.logger.info(msg)
        elif mode == QtCore.QtWarningMsg:
            self.logger.warning(msg)
        elif mode == QtCore.QtCriticalMsg:
            self.logger.critical(msg)
        elif mode == QtCore.QtFatalMsg:
            self.logger.fatal(msg)
        else:
            self.logger.debug(msg)


class WindowHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        InformationWindow('Ошибка', log_entry)
