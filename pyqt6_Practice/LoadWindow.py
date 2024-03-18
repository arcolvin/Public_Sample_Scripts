from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
import sys
import os, inspect


class UI(QWidget):
    def __init__(self):
        super().__init__()

        scriptPath = str(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
        fullPath = f"{scriptPath}/ImportWindow.ui"
        uic.loadUi(fullPath, self)

app = QApplication(sys.argv)

window = UI()
window.show()

sys.exit(app.exec())