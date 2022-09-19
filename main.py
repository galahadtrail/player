from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from player_form import UiWizardPage


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = UiWizardPage()
        self.ui.setup_ui(self)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
