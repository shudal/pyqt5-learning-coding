# -*- coding: utf-8 -*-

'''
主菜单
'''

'''
主菜单即是指
    右键菜单、工具栏、状态栏、菜单栏
'''
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QMenu, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        # 前两个参数表位置，后两个参数表大小
        self.setGeometry(300, 300, 500, 500)

        self.setWindowTitle('StatusBar')
        self.setWindowIcon(QIcon('web.jpg'))

        # 添加一个选项
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        # 悬停时的提示
        exitAction.setStatusTip('Exit application')
        # 绑定退出
        exitAction.triggered.connect(qApp.quit)

        menuBar = self.menuBar()
        # 菜单栏有了一个File栏
        fileMenu = menuBar.addMenu('&File')
        # 这个栏下有个EXIT选项
        fileMenu.addAction(exitAction)

        # 子菜单
        impMenu = QMenu('Import', self)
        impAction = QAction('Import mail', self)
        newAction = QAction('New', self)
        impMenu.addAction(impAction)
        fileMenu.addAction(newAction)
        fileMenu.addMenu(impMenu)

        # 可勾选菜单
        viewMenu = menuBar.addMenu('View')
        viewStatActon = QAction('View status bar', self, checkable=True)
        viewStatActon.setStatusTip('View status bar tip')
        viewStatActon.setChecked(True)
        viewStatActon.triggered.connect(self.toggleMenu)
        viewMenu.addAction(viewStatActon)


        # 工具栏
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        # 添加一个状态栏
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        '''
        
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        # 在两个按钮前面增加弹性空间
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        '''
        self.show()

    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    # 右键菜单
    def contextMenuEvent(self, event):
        cemu = QMenu(self)

        newAction = cemu.addAction("New")
        opnAction = cemu.addAction("Open")
        quitAction = cemu.addAction("Quit")
        action = cemu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAction:
            qApp.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

