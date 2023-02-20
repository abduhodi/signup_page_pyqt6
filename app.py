from widgets.main import QApplication, MainWindow
from sys import argv
from widgets.sign_in.sign_in import SignIn


if __name__ == "__main__":
    app = QApplication(argv)
    sign_up = MainWindow()
    sign_in = SignIn()
    sign_in.show()
    sign_in.signal.sign_up_signal.connect(sign_up.show)
    sign_up.signal.sign_in_signal.connect(sign_in.show)

    app.exec()