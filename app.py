from widgets.main import *
import sys, img
from PyQt6.QtWidgets import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()

    app.exec()