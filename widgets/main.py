from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QCheckBox, QMessageBox, QApplication, QWidget
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import re, requests
from widgets.signals import MySignals
from widgets.check import Check
from widgets.user import User



class MainWindow(QMainWindow):
    def __init__(self, title="Sign up") -> None:
        super().__init__()
        self.setupWindow()
        self.setWindowIcon(QIcon("img/add-user.png"))
        self.setGeometry(500, 150, 300, 400)
        self.setFixedSize(400, 500)
        self.setWindowTitle(title)
        self.signal = MySignals()

    def setupWindow(self):
        style_label = """
        font-size: 18px;
        font-weight: 600;
        """

        style_input = """
        QLineEdit{
            font-size: 18px;
            font-weight: 200;
            border-radius: 5px;
        }
        """

        style_button = """
        QPushButton{
            font-size: 18px;
            font-weight: 500;
            border-radius: 5px;
            background-color: #43b9f4;
        }

        QPushButton:hover{
        background-color: #0ea4ef;
        }

        """
        self.signup_label = QLabel('')
        self.signup_label.setPixmap(QPixmap("img/create-account.png").scaled(100, 100))
        self.signup_label.setFixedSize(100, 100)
     

        signup_layout = QHBoxLayout()
        signup_layout.addStretch()
        signup_layout.addWidget(self.signup_label)
        signup_layout.addStretch()


        self.name_label = QLabel("")
        self.name_label.setPixmap(QPixmap("img/user.png").scaled(25, 25))
        self.name_label.setFixedSize(30, 30)
        # self.name_label.setStyleSheet()

        self.name_input = QLineEdit()
        self.name_input.setFixedSize(300, 35)
        self.name_input.setPlaceholderText("Input your name here")
        self.name_input.setStyleSheet(style_input)

        name_layout = QHBoxLayout()
        name_layout.addStretch()
        name_layout.addSpacing(10)
        name_layout.addWidget(self.name_label)
        name_layout.addWidget(self.name_input)
        name_layout.addSpacing(30)
        name_layout.addStretch()


        self.email_label = QLabel("")
        self.email_label.setPixmap(QPixmap("img/email.png").scaled(25, 25))
        self.email_label.setFixedSize(30, 30)        


        self.email_input = QLineEdit()
        self.email_input.setFixedSize(300, 35)
        self.email_input.setPlaceholderText("example@gmail.com")
        self.email_input.setStyleSheet(style_input)

        email_layout = QHBoxLayout()     
        email_layout.addStretch()
        email_layout.addSpacing(10)
        email_layout.addWidget(self.email_label)
        email_layout.addWidget(self.email_input)
        email_layout.addSpacing(30)
        email_layout.addStretch()


        self.password_label = QLabel("")
        self.password_label.setPixmap(QPixmap("img/padlock.png").scaled(25, 25))
        self.password_label.setFixedSize(30, 30)


        self.password_input = QLineEdit()
        self.password_input.setFixedSize(300, 35)      
        self.password_input.setPlaceholderText("Password")
        self.password_input.setStyleSheet(style_input)
        self.password_input.setEchoMode(QLineEdit().echoMode().Password)

        self.passwd_view = QPushButton(QIcon('./img/hide.png'), '')
        self.passwd_view.setFixedSize(25, 25)
        self.passwd_view.setObjectName("passwd_view_btn")
        self.passwd_view.setStyleSheet("#passwd_view_btn{background: transparent;}")
        self.passwd_view.clicked.connect(self.unhide_password)


        passwd_layout = QHBoxLayout()     
        passwd_layout.addStretch()
        passwd_layout.addSpacing(10)
        passwd_layout.addWidget(self.password_label)
        passwd_layout.addWidget(self.password_input)
        passwd_layout.addWidget(self.passwd_view)
        passwd_layout.addStretch()


        self.telegram_id_label = QLabel("")
        self.telegram_id_label.setPixmap(QPixmap("img/telegram.png").scaled(25, 25))
        self.telegram_id_label.setFixedSize(30, 30)

        self.telegram_id_input = QLineEdit()
        self.telegram_id_input.setFixedSize(300, 35)
        self.telegram_id_input.setPlaceholderText("Telegram Id")
        self.telegram_id_input.setStyleSheet(style_input)

        telegram_id_layout = QHBoxLayout()     
        telegram_id_layout.addStretch()
        telegram_id_layout.addSpacing(10)
        telegram_id_layout.addWidget(self.telegram_id_label)
        telegram_id_layout.addWidget(self.telegram_id_input)
        telegram_id_layout.addSpacing(30)
        telegram_id_layout.addStretch()


        self.terms_conditions_check = QCheckBox("Agree terms and conditions")
        self.terms_conditions_check.setStyleSheet("QCheckBox{font-size: 14px; font-weight: 800;}")

        terms_layout = QHBoxLayout()
        terms_layout.addStretch()
        terms_layout.addWidget(self.terms_conditions_check)
        terms_layout.addStretch()

        self.signup_button = QPushButton("Sign up")
        self.signup_button.setFixedSize(150, 40)
        self.signup_button.setStyleSheet(style_button)
        self.signup_button.clicked.connect(self.signup)


        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setFixedSize(150, 40)
        self.cancel_button.setStyleSheet(style_button)
        self.cancel_button.clicked.connect(self.exit)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.signup_button)
        button_layout.addSpacing(20)
        button_layout.addWidget(self.cancel_button)
        button_layout.addSpacing(10)
        button_layout.addStretch()


        vertical_layout = QVBoxLayout()
        vertical_layout.addStretch()
        vertical_layout.addLayout(signup_layout)
        vertical_layout.addSpacing(20)
        vertical_layout.addLayout(name_layout)
        vertical_layout.addSpacing(10)
        vertical_layout.addLayout(email_layout)
        vertical_layout.addSpacing(10)
        vertical_layout.addLayout(passwd_layout)
        vertical_layout.addSpacing(10)
        vertical_layout.addLayout(telegram_id_layout)
        vertical_layout.addSpacing(5)
        vertical_layout.addLayout(terms_layout)
        vertical_layout.addSpacing(5)
        vertical_layout.addLayout(button_layout)
        vertical_layout.addSpacing(25)
        vertical_layout.addStretch()


        center = QWidget()
        center.setLayout(vertical_layout)
        self.setCentralWidget(center)

    def send_notification(self):
        chat_id = int(self.telegram_id_input.text())
        text = f"You are signed up on Our platform\nYour email: {self.email_input.text()}\nYour password: {self.password_input.text()}"
        url = f"https://api.telegram.org/bot6047953011:AAHuwsHBuRmnOFh_ZvtwZaracowp4jWMPDg/sendMessage?chat_id={chat_id}&text={text}"
        response = requests.post(url)
        print(response.json())
        if response.status_code == 200:
            return True
        return False

    def unhide_password(self):
        if self.password_input.echoMode().name == 'Password':
            self.password_input.setEchoMode(QLineEdit().echoMode().Normal)
            self.passwd_view.setIcon(QIcon("./img/eye.png"))
        elif self.password_input.echoMode().name == 'Normal':
            self.password_input.setEchoMode(QLineEdit().echoMode().Password)
            self.passwd_view.setIcon(QIcon("./img/hide.png"))


    def signup(self):
        if not Check.is_valid_name(self.name_input.text()):
            self.name_input_error = QMessageBox.critical(self, 'Error', 'Name error!')
        elif not Check.is_valid_email(self.email_input.text()):
            self.email_input_error = QMessageBox.critical(self, 'Error', 'Incorrect Email format!')
        elif not Check.is_valid_passwd(self.password_input.text()):
            self.password_error = QMessageBox.critical(self, 'Error', 'Invalid password!\nPassword must have atleast 1 Capital letter, 1 Lowercase letter, 1 number, more than 8 character')
        elif not Check.is_valid_id(self.telegram_id_input.text()):
            self.telegram_id_input_error = QMessageBox.critical(self, 'Error', 'Invalid Telegram ID!')
        elif not self.terms_conditions_check.isChecked():
            self.check_error = QMessageBox.critical(self, 'Error', 'You should agree with Terms and Condition!')
        elif not User.is_registered(self.email_input.text()):
            if self.send_notification():
                user = User(
                            self.name_input.text(), 
                            self.email_input.text(),
                            self.password_input.text(),
                            self.telegram_id_input.text())
                user.register()
                self.name_input.clear()
                self.email_input.clear()
                self.password_input.clear()
                self.telegram_id_input.clear()
                self.terms_conditions_check.setChecked(False)
                self.signedup = QMessageBox.about(self, "Signed up", "You successfully signed up!\nWe have send notification to your telegram")
            else:
                self.check_error = QMessageBox.critical(self, 'Error', 'Telegram ID not found!')
        else:
            QMessageBox.critical(self, "Already registered", "This email already registered!")


    def exit(self):
        self.signal.sign_in_signal.emit()
        self.close()


    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if a0.key() == Qt.Key.Key_Escape.value:
            self.close()