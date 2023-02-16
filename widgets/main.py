from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QCheckBox, QMessageBox, QApplication, QWidget
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import re, requests



class MainWindow(QMainWindow):
    def __init__(self, width=400, height=450, title="Main") -> None:
        super().__init__()
        self.setupWindow()
        self.setGeometry(500, 150, width, height)
        self.setWindowTitle(title)

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

        QPushButton::hover{
        background-color: #0ea4ef;
        }

        """
        self.signup_label = QLabel('SIGN UP')
        # self.signup_label.setFont(QFont("San Serif", 24, 300))
        self.signup_label.setObjectName("signup_label")
        self.signup_label.setStyleSheet("#signup_label{font-size: 24px; font-weight: 600; color: #0ea4ef;}")


        signup_layout = QHBoxLayout()
        signup_layout.addStretch()
        signup_layout.addWidget(self.signup_label)
        signup_layout.addStretch()


        self.name_label = QLabel("Name:")
        self.name_label.setFixedWidth(120)
        self.name_label.setFixedHeight(40)
        self.name_label.setStyleSheet(style_label)

        self.name_input = QLineEdit()
        self.name_input.setFixedWidth(200)
        self.name_input.setFixedHeight(40)
        self.name_input.setPlaceholderText("Input your name here")
        self.name_input.setStyleSheet(style_input)

        name_layout = QHBoxLayout()
        name_layout.addStretch()
        name_layout.addWidget(self.name_label)
        name_layout.addWidget(self.name_input)
        name_layout.addStretch()


        self.email_label  =QLabel("E-mail:")
        self.email_label.setFixedWidth(120)        
        self.email_label.setFixedHeight(40)        
        self.email_label.setStyleSheet(style_label)

        self.email_input = QLineEdit()
        self.email_input.setFixedWidth(200)        
        self.email_input.setFixedHeight(40)        
        self.email_input.setPlaceholderText("example@gmail.com")
        self.email_input.setStyleSheet(style_input)

        email_layout = QHBoxLayout()     
        email_layout.addStretch()
        email_layout.addWidget(self.email_label)
        email_layout.addWidget(self.email_input)
        email_layout.addStretch()


        self.password_label  =QLabel("Password:")
        self.password_label.setFixedWidth(120)      
        self.password_label.setFixedHeight(40)      
        self.password_label.setStyleSheet(style_label)

        self.password_input = QLineEdit()
        self.password_input.setFixedWidth(200)      
        self.password_input.setFixedHeight(40)      
        self.password_input.setPlaceholderText("Password")
        self.password_input.setStyleSheet(style_input)
        self.password_input.setEchoMode(QLineEdit().echoMode().Password)

        self.passwd_view = QPushButton(QIcon('./img/hide.png'), '')
        self.passwd_view.setFixedSize(25, 25)
        self.passwd_view.setObjectName("passwd_view_btn")
        self.passwd_view.setStyleSheet("#passwd_view_btn{background: transparent;}")
        self.passwd_view.clicked.connect(self.unhide_password)

        passwd_view_layout = QHBoxLayout()
        passwd_view_layout.addStretch()
        passwd_view_layout.addSpacing(300)
        passwd_view_layout.addWidget(self.passwd_view)
        passwd_view_layout.addStretch()

        passwd_layout = QHBoxLayout()     
        passwd_layout.addStretch()
        passwd_layout.addWidget(self.password_label)
        passwd_layout.addWidget(self.password_input)
        passwd_layout.addStretch()


        self.telegram_id_label  =QLabel("Telegram ID:")
        self.telegram_id_label.setFixedWidth(120)  
        self.telegram_id_label.setFixedHeight(40)  
        self.telegram_id_label.setStyleSheet(style_label)

        self.telegram_id_input = QLineEdit()
        self.telegram_id_input.setFixedWidth(200)  
        self.telegram_id_input.setFixedHeight(40)  
        self.telegram_id_input.setPlaceholderText("Telegram Id")
        self.telegram_id_input.setStyleSheet(style_input)

        telegram_id_layout = QHBoxLayout()     
        telegram_id_layout.addStretch()
        telegram_id_layout.addWidget(self.telegram_id_label)
        telegram_id_layout.addWidget(self.telegram_id_input)
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
        vertical_layout.addLayout(passwd_view_layout)
        vertical_layout.addLayout(telegram_id_layout)
        vertical_layout.addSpacing(5)
        vertical_layout.addLayout(terms_layout)
        vertical_layout.addSpacing(5)
        vertical_layout.addLayout(button_layout)
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
        echo_mode = str(self.password_input.echoMode()).split('.')[-1]
        if echo_mode == 'Password':
            self.password_input.setEchoMode(QLineEdit().echoMode().Normal)
            self.passwd_view.setIcon(QIcon("./img/eye.png"))
        elif echo_mode == 'Normal':
            self.password_input.setEchoMode(QLineEdit().echoMode().Password)
            self.passwd_view.setIcon(QIcon("./img/hide.png"))


    def signup(self):
        if len(self.name_input.text()) < 1:
            self.name_input_error = QMessageBox.critical(self, 'Error', 'Name must be entered!')
        elif not re.match(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", self.email_input.text()):
            self.email_input_error = QMessageBox.critical(self, 'Error', 'Incorrect Email format!')
        elif len(self.password_input.text()) < 8:
            self.password_error = QMessageBox.critical(self, 'Error', 'Invalid password format!')
        elif not (7 < len(self.telegram_id_input.text()) < 10 and self.telegram_id_input.text().isdigit()):
            self.telegram_id_input_error = QMessageBox.critical(self, 'Error', 'Invalid Telegram ID format!')
        elif not self.terms_conditions_check.isChecked():
            self.check_error = QMessageBox.critical(self, 'Error', 'You should agree with Terms and Condition!')
        else:
            if self.send_notification():
                self.name_input.clear()
                self.email_input.clear()
                self.password_input.clear()
                self.telegram_id_input.clear()
                self.terms_conditions_check.setChecked(False)
                self.signedup = QMessageBox.about(self, "Signed up", "You successfully signed up!\nWe have send notification to your telegram")
            else:
                self.check_error = QMessageBox.critical(self, 'Error', 'Telegram ID not found!')


    def exit(self):
        QApplication.quit()
