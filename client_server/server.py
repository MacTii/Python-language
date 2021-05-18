from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import QPoint
import socket

class Server(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kółeczko - Serwer")
        self.setGeometry(500, 200, 350, 400)

        #create a menu of server
        self.createMenu()

        #show info about the server
        self.showInfo()

        ########################## socket
        HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
        PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print("Connected by", addr)
                while True:
                    data = conn.recv(1024)
                    print(data)
                    if not data:
                        break
                    conn.sendall(data)

    def createActions(self):
        self.connectAction = QAction("Połącz z serwerem", self)
        self.connectAction.triggered.connect(self.actionClicked)
        self.connectAction.setCheckable(True)

    def createMenu(self):
        menuBar = self.menuBar()
        fileMenu = QMenu("Serwer", self)
        menuBar.addMenu(fileMenu)

        self.createActions()
        fileMenu.addAction(self.connectAction)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
        p = QPoint(170, 210)
        painter.drawEllipse(p, 100, 100)
        painter.end()
    
    def actionClicked(self):
        action = self.sender()
        if action.isChecked() == True:
            self.label.setText('Serwer jest włączony')
        else:
            self.label.setText('Serwer jest wyłączony')
    
    def showInfo(self):
        self.label = QLabel(self)
        self.label.setText('Serwer jest wyłączony')
        self.label.move(10, 35)    
        self.label.adjustSize()


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    server = Server()
    server.show()
    sys.exit(app.exec_())
