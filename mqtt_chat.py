import sys
import paho.mqtt.client as titties
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QPlainTextEdit, QHBoxLayout, \
    QVBoxLayout, QApplication, QTextEdit


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.windowWidth = 800
        self.windowHeight = 500

        self.client = self.connection()
        self.currentTopic = ""

        self.setWindowTitle("Chat - MQTT")
        self.resize(self.windowWidth, self.windowHeight)

        self.topicTextbox = QLineEdit(self) # button "Połącz"
        self.topicSendButton = QPushButton("Połącz", self)
        self.topicSendButton.clicked.connect(self.setTopic)

        self.messagesArea = QTextEdit(self)
        self.messagesArea.setReadOnly(True)
        self.messageTextbox = QLineEdit(self)
        self.messageTextbox.returnPressed.connect(self.sendMessage)
        self.messageSendButton = QPushButton("Wyślij wiadomość", self)
        self.messageSendButton.clicked.connect(self.sendMessage)

        self.topicLayout = QVBoxLayout(self)
        self.topicLayout.addWidget(self.topicTextbox)
        self.topicLayout.addWidget(self.topicSendButton)

        self.messageSendLayout = QHBoxLayout(self)
        self.messageSendLayout.addWidget(self.messageTextbox)
        self.messageSendLayout.addWidget(self.messageSendButton)

        self.messageLayout = QVBoxLayout(self)
        self.messageLayout.addWidget(self.messagesArea)
        self.messageLayout.addLayout(self.messageSendLayout)

        self.mainLayout = QHBoxLayout(self)
        self.mainLayout.addLayout(self.topicLayout)
        self.mainLayout.addLayout(self.messageLayout)

        self.mainContainer = QWidget()
        self.mainContainer.setLayout(self.mainLayout)

        self.setCentralWidget(self.mainContainer)

    def message(self, client, userdata, msg):
        msg.payload = msg.payload.decode("utf-8") # receving messages
        self.messagesArea.append(str(msg.topic) + ": " + str(msg.payload))
        self.update()

    def connect(self, client, userdata, flags, rc):
        print("Połączyłeś się z " + str(rc))

    def connection(self):
        client = titties.Client()
        client.msg = self.message
        client.cnct = self.connect
        clientThread = MQTTThread(client) # add new client
        clientThread.start()
        return clientThread

    def setTopic(self):
        self.currentTopic = self.topicTextbox.text() # text box
        self.client.client.subscribe(self.currentTopic)
        print("Połącz z: " + self.currentTopic)

    def sendMessage(self):
        messageText = self.messageTextbox.text()
        self.messageTextbox.clear()

        self.client.client.publish(self.currentTopic, messageText)
        print("Wysłałeś wiadomość " + messageText)


class MQTTThread(QThread):

    def __init__(self, client):
        super(MQTTThread, self).__init__()
        self.client = client

    def run(self):
        self.client.connect("test.mosquitto.org", 1883, 60)
        self.client.loop_forever()


if __name__ == '__main__':
    application = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(application.exec_())
