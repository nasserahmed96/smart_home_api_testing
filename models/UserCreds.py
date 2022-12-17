class UserCreds:
    def __init__(self, username='', password=''):
        self.username = username
        self.password = password

    def set_username(self, username: str):
        self.username = username

    def get_username(self):
        return self.username

    def set_password(self, password: str):
        self.password = password

    def get_password(self):
        return self.password