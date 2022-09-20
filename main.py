from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
from player_form import UiWizardPage


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = UiWizardPage()
        self.ui.setup_ui(self)
        self.setObjectName('MainWindow')
        self.setWindowIcon(QIcon('images/title_icon'))


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
