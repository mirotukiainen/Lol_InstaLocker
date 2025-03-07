import sys
import PyQt5.QtWidgets as qt
import time
from func.locate_champion import search
class MainWindow(qt.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("League of Legends | InstaLocker")
        self.setGeometry(100, 100, 300, 150)

        self.input_field = qt.QLineEdit(self)
        self.button = qt.QPushButton("Submit", self)
        self.button.clicked.connect(self.on_button_click)

        layout = qt.QVBoxLayout()
        layout.addWidget(self.input_field)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def on_button_click(self):
        champion = self.input_field.text()
        print(f"Input: {champion}")
        search(champion)

def run_application():
    app = qt.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    time.sleep(1)
    sys.exit(app.exec_())
