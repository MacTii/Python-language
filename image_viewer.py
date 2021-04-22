from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QWidget, QSizePolicy, QMenu, QAction
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect

class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        self.resize(800, 600)

        self.i = 0
        self.tab = []

        #Insert images to table
        self.insertImages()

        #Set widget
        self.widget = QWidget()

        #Set image
        self.setImage()

        #Set buttons
        self.setPrevButton()
        self.setNextButton()

        #Set central widget
        self.setCentralWidget(self.widget)

        #Name buttons
        self.setNameButtons()

        #Function buttons
        self.nextButton.clicked.connect(self.showNext)
        self.prevButton.clicked.connect(self.showPrev)

        self.createMenuBar()
        #self.createActions()

    def setImage(self):
        self.image = QLabel(self.widget)
        self.image.setGeometry(QRect(0, 0, 840, 510))
        self.pixmap = QPixmap(self.tab[self.i])
        self.image.setPixmap(self.pixmap)
        self.image.setScaledContents(True)

    def insertImages(self): 
        self.tab.append('./imag/image.jpg')
        self.tab.append('./imag/image1.jpg')
        self.tab.append('./imag/image2.jpg')
        self.tab.append('./imag/image3.jpg')

    def setPrevButton(self):
        self.prevButton = QPushButton(self.widget)
        self.prevButton.setGeometry(QRect(0, 510, 410, 50))
        #self.prevButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def setNextButton(self):
        self.nextButton = QPushButton(self.widget)
        self.nextButton.setGeometry(QRect(410, 510, 410, 50))
        #self.nextButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def setNameButtons(self):
        self.prevButton.setText("PREV")
        self.nextButton.setText("NEXT")

    def showPrev(self):
        self.i -= 1
        #print(self.i)
        if self.i == -1:
            self.i = 0
        pixmap = QPixmap(self.tab[self.i])
        self.image.setPixmap(pixmap)

    def showNext(self):
        self.i += 1
        #print(self.i)
        #print(len(self.tab))
        if self.i == len(self.tab):
            self.i = len(self.tab) - 1
        pixmap = QPixmap(self.tab[self.i])
        self.image.setPixmap(pixmap)
    
    def createMenuBar(self):
        menuBar = self.menuBar()
        calculatorSelectionMenu = menuBar.addMenu("&File")
        viewMenu = menuBar.addMenu("&View")
        helpMenu = menuBar.addMenu("&Help")

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    imageViewer = ImageViewer()
    imageViewer.show()
    sys.exit(app.exec_())
