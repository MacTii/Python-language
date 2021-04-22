from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QWidget, QSizePolicy, QMenu, QAction, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect

class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        self.resize(800, 600)

        self.i = 0
        self.tab = []
        self.scaleFactor = 1.0

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

        #Menu with actions
        self.createActions()
        self.createMenuBar()

    def setImage(self):
        self.image = QLabel(self.widget)
        self.image.setGeometry(QRect(0, 0, 840, 510)) # 840 510
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
    
    def createActions(self):
        self.openAct = QAction("&Open...", self, shortcut="Ctrl+O") # triggered=self.open
        self.printAct = QAction("&Print...", self, shortcut="Ctrl+P", enabled=False) # triggered=self.print_
        self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q", triggered=self.close)

        self.zoomInAct = QAction("Zoom &In (25%)", self, shortcut="Ctrl++", enabled=True, triggered=self.zoomIn) # triggered=self.zoomIn
        self.zoomOutAct = QAction("Zoom &Out (25%)", self, shortcut="Ctrl+-", enabled=True, triggered=self.zoomOut) # triggered=self.zoomOut
        self.normalSizeAct = QAction("&Normal Size", self, shortcut="Ctrl+S", enabled=True, triggered=self.normalSize) # triggered=self.normalSize
        #self.fitToWindowAct = QAction("&Fit to Window", self, enabled=True, checkable=True, shortcut="Ctrl+F") # triggered=self.fitToWindow

        self.aboutAct = QAction("&About", self, triggered=self.about) # triggered=self.about

    def createMenuBar(self):
        self.fileMenu = QMenu("&File", self)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.printAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.viewMenu = QMenu("&View", self)
        self.viewMenu.addAction(self.zoomInAct)
        self.viewMenu.addAction(self.zoomOutAct)
        self.viewMenu.addAction(self.normalSizeAct)
        #self.viewMenu.addSeparator()
        #self.viewMenu.addAction(self.fitToWindowAct)

        self.helpMenu = QMenu("&Help", self)
        self.helpMenu.addAction(self.aboutAct)

        menuBar = self.menuBar()
        menuBar.addMenu(self.fileMenu)
        menuBar.addMenu(self.viewMenu)
        menuBar.addMenu(self.helpMenu)

    def normalSize(self):
        self.image.setGeometry(QRect(0, 0, 840, 510)) # 840 510
        #self.scaleFactor = 1.0
    
    def zoomIn(self):
        self.scaleImage(1.25)

    def zoomOut(self):
        self.scaleImage(0.8)
    
    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.image.resize(self.scaleFactor * self.image.pixmap().size())

    #def fitToWindow(self):
    #    fitToWindow = self.fitToWindowAct.isChecked()
    #    self.scrollArea.setWidgetResizable(fitToWindow)
    #    if not fitToWindow:
    #        self.normalSize()
    #
    #    self.updateActions()

    def about(self):
        QMessageBox.about(self, "About Image Viewer",
                          "<p><b>Image Viewer</b> jest to aplikacja GUI oparta o zadanie z przedmiotu KCK</p>")

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    imageViewer = ImageViewer()
    imageViewer.show()
    sys.exit(app.exec_())
