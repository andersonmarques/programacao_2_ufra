import numpy as np
import statistics as st

class Matriz:
    
    def __init__(self, n=None, m=None) -> None:
        self.linha = n
        self.coluna = m

    @property
    def valores(self):
        return self.__valores
    
    @valores.setter
    def valores(self, valores:np.ndarray):
        self.__valores = valores

    @property
    def coluna(self):
        return self.__coluna

    @coluna.setter
    def coluna(self, coluna):
        if coluna <= 0:
            print("Erro!")
        else:
            self.__coluna = coluna

    @property
    def linha(self):
        return self.__linha

    @linha.setter
    def linha(self, n):
        if n <= 0:
            print("Erro!")
        else:
            self.__linha = n

    def criar_matriz_nula(self):
        return np.zeros((self.linha, self.coluna))

    def calcular_media(self):
        pass