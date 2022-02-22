from model.ordem import Ordem

class Familia:
    def __init__(self, nome = None, ordem = None) -> None:
        self.nome = nome
        self.ordem = ordem
        self.lista_generos = None
    
    def __str__(self):
        return f'Familia: {self.__nome}'

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def ordem(self) -> Ordem:#indica que retornara um objeto Ordem
        return self.__ordem

    @ordem.setter
    def ordem(self, value):
        self.__ordem = value

    @property
    def lista_generos(self):
        return self.__generos

    @lista_generos.setter
    def lista_generos(self, value):
        # if not bool(value):
        #     self.__generos = self.__generos
        # elif value is None:
        self.__generos = []
        # else:
        #     self.__generos = self.__generos


