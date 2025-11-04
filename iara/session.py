class UserSession:
    def __init__(self):
        self.cod_empresa = None

    def login(self, user_data):
        self.cod_empresa = user_data.get('cod_empresa')

    def logout(self):
        self.cod_empresa = None

current_user = UserSession()