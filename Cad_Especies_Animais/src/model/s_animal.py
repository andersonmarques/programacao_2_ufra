class S_Animal:
    def __init__(self, id = None, nome = None, idade = None, especie = None, 
    subespecie = None, classificacao = None, habitat = None) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.subespecie = subespecie
        self.classificacao = classificacao
        self.habitat = habitat
        self.erro = ''

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if nome is not None and len(nome) != 0:
            self.__nome = nome
        else:
            self.erro = 'O campo nome é obrigatório.'

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        if idade is not None and int(idade) > -1:
            self.__idade = idade
        else:
            self.erro = 'O campo idade é obrigatório.'

    @property
    def especie(self):
        return self.__especie

    @especie.setter
    def especie(self, especie):               
        if especie == '---':
            self.erro = 'O campo especie é obrigatório.'
        else:
            self.__especie = especie
        
    @property
    def subespecie(self):
        return self.__subespecie

    @subespecie.setter
    def subespecie(self, subespecie):
        if subespecie == '---':
        # eh porque o ususario escolheu os '---'
            self.erro = 'O campo subespecie é obrigatório.'
        else:
            self.__subespecie = subespecie

    @property
    def classificacao(self):
        return self.__classificacao

    @classificacao.setter
    def classificacao(self, classificacao):
        if classificacao == '---':
            self.erro = 'O campo classificacao é obrigatório.'
        else:
            self.__classificacao = classificacao

    @property
    def habitat(self):
        return self.__habitat

    @habitat.setter
    def habitat(self, habitat):
        if habitat == '---':
            self.erro = 'O campo habitat é obrigatório.'
        else:
            self.__habitat = habitat

    def __str__(self) -> str:
        return f'Animal: {self.id} | {self.subespecie}'