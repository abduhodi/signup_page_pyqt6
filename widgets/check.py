import re
class Check:
    # @staticmethod
    def is_valid_email(self):
        if re.match(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", self):
            return True
        else:
            return False

    def is_valid_name(self):
        if len(self) < 2 or (not self.isalpha()):
            return False
        else:
            return True

    def is_valid_passwd(self):
        if len(self) < 8:
            return False
        if not re.match(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}", self):
            return False
        else:
            return True

    def is_valid_id(self):
        if not (8 < len(self) < 11 and self.isdigit()):
            return  False
        else:
            return True




# text = "m"
# print(Check.is_valid_name(text))


        # if len(self.name_input.text()) < 1 and not self.name_input.text().isalpha():
        #     self.name_input_error = QMessageBox.critical(self, 'Error', 'Name must be entered!')
        # elif not re.match(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", self.email_input.text()):
        #     self.email_input_error = QMessageBox.critical(self, 'Error', 'Incorrect Email format!')
        # elif len(self.password_input.text()) < 8:
        #     self.password_error = QMessageBox.critical(self, 'Error', 'Invalid password format!')
        # elif not (7 < len(self.telegram_id_input.text()) < 11 and self.telegram_id_input.text().isdigit()):
        #     self.telegram_id_input_error = QMessageBox.critical(self, 'Error', 'Invalid Telegram ID format!')
        # elif not self.terms_conditions_check.isChecked():
        #     self.check_error = QMessageBox.critical(self, 'Error', 'You should agree with Terms and Condition!')