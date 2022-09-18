from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        self.centralWidget(button)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
