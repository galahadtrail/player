from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        button.setFixedSize(200, 200)
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)

        self.setFixedSize(400, 300)

        self.setCentralWidget(button)

    @staticmethod
    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self):
        print(self.button_is_checked)
        self.button_is_checked = False if self.button_is_checked else True


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
