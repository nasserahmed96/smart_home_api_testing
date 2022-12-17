from services import Request
from models.UserCreds import UserCreds
from services.Request import Request

class Authentication:
    def __init__(self, user_creds: UserCreds):
        self._user_creds = user_creds

    def set_user_creds(self, user_creds):
        self._user_creds = user_creds

    def get_user_creds(self):
        return self._user_creds

    def authenticate(self):
        request = Request(url='home-resident/authenticate', body={
            "username": self._user_creds.get_username(),
            "password": self._user_creds.get_password()
        })
        return request.send_post_request()


if __name__ == '__main__':
    authenticate = Authentication(UserCreds(username='nasser', password='admin'))
    print(authenticate.authenticate())