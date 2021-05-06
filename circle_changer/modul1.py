from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyDialog(QDialog):
    
    def __init__(self,parent=None):
        super().__init__()
        
    def showDialogColor(self):
        items = ("czerwony", "zielony", "błękitny", "żółty")
        item, result = QInputDialog.getItem(self, 'Ustaw kolor okna głównego','Wybierz kolor', items, 0, False)
        if item == 'czerwony':
            self.setStyleSheet("background-color: red")
        if item == 'zielony':
            self.setStyleSheet("background-color: lime")
        if item == 'błękitny':
            self.setStyleSheet("background-color: blue")
        if item == 'żółty':
            self.setStyleSheet("background-color: yellow")
        
        