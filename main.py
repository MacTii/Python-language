from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget, QApplication, QMainWindow, QWidget, QRadioButton, QFrame
# from PySide import QtGui # color buttons

import sys

from functools import partial

ERROR_MSG = 'ERROR'

class Calculator(QMainWindow):
    """Calculator's View (GUI)."""
    def __init__(self):

        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Kalkulator')
        #self.setFixedSize(235, 235)

        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()

        # Set the central widget
        self._centralWidget = QWidget(self)
        self._centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(self._centralWidget)

        # Create the display and the buttons
        self._createDisplay()
        self._createButtons()

        # Create the display menu
        self._createMenuBar()

    def _createDisplay(self):
        """Create the display."""
        # Create the display widget
        self.display = QLineEdit()

        # Set some display's properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        # Add the display to the general layout
        self.generalLayout.addWidget(self.display)

    def _createMenuBar(self):
        menuBar = self.menuBar()
        calculatorSelectionMenu = menuBar.addMenu("&E\u0332dycja")
        viewMenu = menuBar.addMenu("&W\u0332idok")
        helpMenu = menuBar.addMenu("&Pomoc\u0332")

    def onClicked(self):
        radioButton = self.sender()

    def _createButtons(self):

        """Create the buttons."""
        self.buttons = {}
        buttonsLayout = QGridLayout()

        """frame = QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setLineWidth(0.6)"""

        radiobutton1 = QRadioButton("Stopnie")
        radiobutton1.setChecked(True)
        radiobutton1.toggled.connect(self.onClicked)
        buttonsLayout.addWidget(radiobutton1, 0, 2)

        radiobutton2 = QRadioButton("Radiany")
        radiobutton2.toggled.connect(self.onClicked)
        buttonsLayout.addWidget(radiobutton2, 0, 3)

        radiobutton3 = QRadioButton("Gradusy")
        radiobutton3.toggled.connect(self.onClicked)
        buttonsLayout.addWidget(radiobutton3, 0, 4)
        
        # Button text | position on the QGridLayout
        buttons = {'Backspace': (1, 1),
                   'CE': (1, 2),
                   'C': (1, 3),
                   '=': (1, 4),
                   'MC': (2, 0),
                   '7': (2, 1),
                   '8': (2, 2),
                   '9': (2, 3),
                   '/': (2, 4),
                   'MR': (3, 0),
                   '4': (3, 1),
                   '5': (3, 2),
                   '6': (3, 3),
                   '*': (3, 4),
                   'MS': (4, 0),
                   '1': (4, 1),
                   '2': (4, 2),
                   '3': (4, 3),
                   '-': (4, 4),
                   'M+': (5, 0),
                   '0': (5, 1),
                   '+/-': (5, 2),
                   '.': (5, 3),
                   '+': (5, 4),
                  }

        # Create the buttons and add them to the grid layout
        j=0
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            #self.buttons[btnText].setFixedSize(40, 40)
            if (btnText in "7894561230." or btnText == '+/-'):
                self.buttons[btnText].setStyleSheet('QPushButton {; color: blue;}')
            else:
                self.buttons[btnText].setStyleSheet('QPushButton {; color: red;}')
            #if(btnText == 'Backspace'):
                #self.buttons[btnText].setFixedSize(80, 40)
            self.buttons[btnText].setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1], alignment=QtCore.Qt.AlignRight)
            #print(pos[0],pos[1])
            
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText('')

# Create a Controller class to connect the GUI and the model
class CalculatorControl:
    """PyCalc Controller class."""
    def __init__(self, model, view):
        """Controller initializer."""
        self._evaluate = model
        self._view = view

        # Connect signals and slots
        self._connectSignals()

    def _calculateResult(self):
        """Evaluate expressions."""
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C', 'Backspace', 'CE', 'MC', 'MR', 'MS', 'M+', '+/-'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)

# Create a Model to handle the calculator's operation
def evaluateExpression(expression):
    """Evaluate an expression."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result

# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)

    # Show the calculator's GUI
    view = Calculator()
    view.show()

    # Create instances of the model and the controller
    model = evaluateExpression
    CalculatorControl(model=model, view=view)

    # Execute the calculator's main loop
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()
