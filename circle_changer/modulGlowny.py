from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QIcon
import sys
from PyQt5.QtCore import QPoint
from PyQt5.Qt import Qt

from modul1 import MyDialog

class modulGlowny(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialogi")
        self.setGeometry(500, 200, 1000, 800)
        self.setStyleSheet("background-color: gray;")
        self.setWindowIcon(QIcon('logo.png'))
        self.createMenu()
        self.show()

    def createActions(self):
        self.colorAction = QAction("Kolor okna głównego", self)
        self.colorAction.triggered.connect(lambda: MyDialog.showDialogColor(self))
        self.sizeAction = QAction("Ustaw kola", self)
        self.sizeAction.triggered.connect(lambda: modul2())

    def createMenu(self):
        menuBar = self.menuBar()
        fileMenu = QMenu("Dialog", self)
        self.createActions()
        menuBar.addMenu(fileMenu)
        menuBar.setStyleSheet("background-color: none")
        fileMenu.setStyleSheet("background-color: none")
        fileMenu.addAction(self.colorAction)
        fileMenu.addAction(self.sizeAction)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        p = QPoint(500, 410)
        painter.drawEllipse(p, 200, 200)
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        painter.drawEllipse(p, 125, 125)
        painter.end()

App = QApplication(sys.argv)

run = modulGlowny()

sys.exit(App.exec())