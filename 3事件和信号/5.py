# -*- coding: utf-8 -*-

'''
信号发送
    鼠标点击事件
'''
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

class Communicate(QObject):
    closeApp = pyqtSignal()
class Exmaple(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('emit signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exmaple()
    sys.exit(app.exec_())