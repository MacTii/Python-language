from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import QPoint
import socket


class Client(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kółeczko - Klient")
        self.setGeometry(500, 200, 350, 400)

        # radius of circle
        self.radius = 0

        # create a menu of client
        self.createMenu()

        # create a slider to change size of circle
        self.createSlider()

        ######################## socket
        HOST = '127.0.0.1'  # The server's hostname or IP address
        PORT = 65432        # The port used by the server

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            output = str(self.radius)
            s.sendall(output.encode('utf-8'))
            #s.sendall(b'Hello')
            data = s.recv(1024)

        print('Received', repr(data))

    def createActions(self):
        self.connectAction = QAction("Połącz z serwerem", self)

    def createMenu(self):
        menuBar = self.menuBar()
        fileMenu = QMenu("Połączenie", self)
        self.createActions()
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.connectAction)

    def createSlider(self):
        slider = QSlider(Qt.Horizontal, self)
        slider.setGeometry(30, 40, 300, 30)
        slider.valueChanged.connect(self.updateLabel)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
        p = QPoint(170, 210)
        painter.drawEllipse(p, 25 + self.radius, 25 + self.radius)
        painter.end()

    def updateLabel(self, value):
        self.radius = value
        self.update()


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    client = Client()
    client.show()
    sys.exit(app.exec_())
