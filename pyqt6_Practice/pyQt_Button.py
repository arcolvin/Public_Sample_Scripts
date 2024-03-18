from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

class Window (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Button & Label")
        self.setWindowIcon (QIcon("qt.png"))
        self.setGeometry(500,200,500,400)

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())