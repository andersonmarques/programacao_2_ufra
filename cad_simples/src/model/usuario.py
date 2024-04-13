class Usuario:
    def __init__(self, nome = None, email = None, senha = None):
        self.erro_gui = ''
        self.nome = nome
        self.email = email
        self.senha = senha

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if nome == '':
            self.erro_gui = 'Nome não pode ser vazio'
        else:
            self.__nome = nome

    def __str__(self):
        return f'Nome: {self.nome}, Email: {self.email}, Senha: {self.senha}'