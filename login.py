import bcrypt


class User:
    def __init__(self, username, password, salt):
        self.__username = username
        self.__salt = salt
        self.__dummy_password = password.encode("utf-8")
        self.__password = self.encrypt_password()
        print(self.__password)

    def encrypt_password(self):
        return bcrypt.hashpw(self.__dummy_password, self.__salt)


salt = bcrypt.gensalt()
User("Sourav", "Pass123", salt)
User("Sourav", "Pass123", salt)