# -*- coding: utf-8 -*-

'''
绝对定位
'''
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        lbl1 = QLabel('Zetcode', self)
        # x,y坐标的原点是程序的左上角
        lbl1.move(15, 10)
        lb12 = QLabel('tutorials', self)
        lb12.move(35, 40)
        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('绝对定位')
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())