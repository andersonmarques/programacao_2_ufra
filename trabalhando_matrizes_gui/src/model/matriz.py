import numpy as np

class Matriz:
    
    def __init__(self, m=None, n=None) -> None:
        self.linha = m
        self.coluna = n
        self.valores = self.__criar_matriz_nula()
        self.erro_matriz = ''

    def mesma_ordem(self, X) -> bool: 
        mesma_ordem = False
        try:
            if self.linha == X.linha and self.coluna == X.coluna:
                mesma_ordem = True
        except :
            self.erro_matriz = 'ERRO! A matriz X nao pertence a classe Matriz'
            print('----- ERRO! -----\n A matriz X nao pertence a classe Matriz')
        finally:
            return mesma_ordem
    
    def is_quadrada(self) -> bool:
        quadrada = False
        if self.linha == self.coluna:
            quadrada = True
        
        return quadrada

    def ordem(self) -> int:
        if self.is_quadrada():
            return int(self.linha)
        else:
            return -1

    def __criar_matriz_nula(self) -> np.ndarray:
        return np.zeros((self.linha, self.coluna))        

    #-------------- propriedades --------------
    @property
    def valores(self):
        return self.__valores
    
    @valores.setter
    def valores(self, valores):
        M_int = self.__criar_matriz_nula()
        for i in range(0, len(M_int)):
            for j in range(0, len(M_int[0])):
                M_int[i][j] = int(valores[i][j])
        self.__valores = M_int

    @property
    def coluna(self):
        return self.__coluna

    @coluna.setter
    def coluna(self, coluna):
        if coluna <= 0:
            self.erro_matriz = 'Erro! Nao ha matriz com zero colunas'
            print("----- Erro! -----\n 'Erro! Nao ha matriz com zero colunas'")
        else:
            self.__coluna = coluna#8

    @property
    def linha(self):
        return self.__linha

    @linha.setter
    def linha(self, n):
        if n <= 0:
            self.erro_matriz = 'Erro! Nao ha matriz com zero linhas'
            print("----- Erro! -----\n 'Erro! Nao ha matriz com zero linhas'")
        else:
            self.__linha = n#4

    @property
    def erro_matriz(self):
        return self.__erro_matriz

    @erro_matriz.setter
    def erro_matriz(self, msg):
        self.__erro_matriz = msg
