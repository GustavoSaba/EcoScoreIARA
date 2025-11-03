class UserSession:
    def __init__(self):
        self.cod_empresa = None
        self.nome_empresa = None
        self.email = None
        self.cod_login = None
        self.is_logged_in = False

    def login(self, user_data):
        self.cod_empresa = user_data.get('cod_empresa')
        self.nome_empresa = user_data.get('empresa_nome') # Pega o nome da resposta
        self.email = user_data.get('empresa_email')
        self.senha = user_data.get('empresa_senha')
        self.is_logged_in = True

    def logout(self):
        self.cod_empresa = None
        self.nome_empresa = None
        self.email = None
        self.senha = None
        self.is_logged_in = False

current_user = UserSession()