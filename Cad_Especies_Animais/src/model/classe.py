class Classe:

    def __init__(self, nome = None) -> None:
        self.nome = nome
        self.lista_ordens = None

    def __str__(self) -> str:
        return f'Classe: {self.nome}'

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def lista_ordens(self):
        return self.__ordens

    @lista_ordens.setter
    def lista_ordens(self, value):
        self.__ordens = []
