from PyQt6.QtCore import QObject, pyqtSignal

class MySignals(QObject):
    sign_in_signal = pyqtSignal()
    sign_up_signal = pyqtSignal()