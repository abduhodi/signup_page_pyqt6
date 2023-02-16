from widgets.main import QApplication, MainWindow
from sys import argv


if __name__ == "__main__":
    app = QApplication(argv)
    main = MainWindow()
    main.show()

    app.exec()