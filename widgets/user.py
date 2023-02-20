class User:
    def __init__(self, name: str, email: str, passwd: str, telegramId: int) -> None:
        self.name = name,
        self.email = email,
        self.passwd = passwd,
        self.telegramId = telegramId


    def register(self):
        try:
            with open("users.csv", "a") as f:
                data = f"{self.name[0]};{self.email[0]};{self.passwd[0]};{self.telegramId}"
                f.write(data + "\n")
        except:
            print("Registeration failed")
        else:
            print("Registration success")
    
    def is_registered(email: str, passwd: str):
        with open("users.csv", "r") as f:
            users = f.readlines()
            users = [user.split(";") for user in users]
            for user in users:
                if email == user[1] and passwd == user[2]:
                    return True
            return None

            
