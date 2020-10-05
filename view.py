from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
class GUI(QMainWindow):
    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()

        # Set some main window's properties
        self.setWindowTitle('Calculator')
        self.setFixedSize(235, 235)

        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()

        # Set the central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

        self._centralWidget.setLayout(self.generalLayout)

        # Create the display and the buttons
        self._createDisplayLED()
        self._createButtons()

