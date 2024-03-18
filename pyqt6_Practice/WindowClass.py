from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Window Title")
        self.setWindowIcon(QIcon("qt.png"))
        # self.setFixedHeight(200)
        # self.setFixedWidth(200)
        # self.setGeometry(500,300,400,300)
        
        stylesheet = (
            'background-color:red'
        )

        self.setStyleSheet(stylesheet)


app = QApplication([])
window = Window()

window.show()

sys.exit(app.exec())