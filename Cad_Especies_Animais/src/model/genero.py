from model.familia import Familia

class Genero:
    def __init__(self, nome = None, familia = None) -> None:
        self.nome = nome
        self.familia = familia

    def __str__(self) -> str:
        return f'Genero: {self.__nome}'

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def familia(self) -> Familia:
        return self.__familia

    @familia.setter
    def familia(self, value):
        self.__familia = value
