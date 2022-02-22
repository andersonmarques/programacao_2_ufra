from model.classe import Classe


class Ordem:
    def __init__(self, nome = None, classe = None) -> None:
        self.nome = nome
        self.classe = classe
        self.lista_familias = None
    
    def __str__(self):
        return f'Ordem: {self.__nome}'
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def classe(self) -> Classe:
        return self.__classe

    @classe.setter
    def classe(self, value):
        self.__classe = value

    @property
    def lista_familias(self):
        return self.__familias

    @lista_familias.setter
    def lista_familias(self, value):
        self.__familias = []
