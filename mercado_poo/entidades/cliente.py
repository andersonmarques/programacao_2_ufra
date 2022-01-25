import re #modulo de expressoes regulares (regular expressions)

class Cliente:

    def __init__(self, nome = None, cpf = None, endereco = None, bairro = None, email = None, fone = None, categoria = None):
        self.nome = nome 
        self.cpf = cpf 
        self.endereco = endereco 
        self.bairro = bairro
        self.email = email
        self.fone = fone
        self.categoria = categoria
        self.erro_validacao = ''

    def __cpf_valido(self, cpf):
        valido = False
        mesmo_num = True
        for i in range(0, len(cpf) - 1):
            if cpf[i] != cpf[i + 1]:
                mesmo_num = False
                break
        if mesmo_num == True or len(cpf) != 11:
            return valido
        
        soma1 = 0       
        j = 10 
        for i in range(0, len(cpf) - 2):
            if j >= 2:
                soma1 += int(cpf[i]) * j
                j -= 1
                
        resto1 = (soma1 * 10) % 11

        if resto1 == 10:
            resto1 = 0

        soma2 = 0
        x = 11
        for i in range(0, len(cpf) - 1):
            if x >= 2:
                soma2 += int(cpf[i]) * x
                x -= 1

        resto2 = (soma2 * 10) % 11            
        if resto2 == 10:
            resto2 = 0

        if resto1 == int(cpf[9]) and resto2 == int(cpf[10]):
            valido = True
        
        return valido

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if nome != None and len(nome) != 0:
            self.__nome = nome
        else:
            self.erro_validacao = 'O campo "nome" é obrigatório!'

    @property
    def cpf(self):#ex de CPF valido: 17110602087
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if cpf != None:
            if self.__cpf_valido(cpf):
                self.__cpf = cpf
            else:
                self.erro_validacao = 'CPF inválido!'    
        else:
            self.erro_validacao = 'O campo "CPF" é obrigatório!'
    
    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if email != None:
            if re.match(r"^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$", email):
                self.__email = email
            else:
                self.erro_validacao = 'E-mail inválido!'
        else:
            self.erro_validacao = 'O campo "E-mail" é obrigatório!'

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, fone):
        self.__fone = fone

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        if categoria != "-- Categoria --":
            self.__categoria = categoria
        else:
            self.erro_validacao = 'O campo "Categoria" é obrigatório!'