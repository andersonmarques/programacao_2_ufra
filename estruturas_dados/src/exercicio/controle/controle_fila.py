from typing import Deque
from modelo.nodo import Nodo
from collections import deque

class Controle_Fila:
    
    def __init__(self) -> None:
        self.fila = None
        
    def     entrar_fila(self, nodo):
        '''
        Metodo responsavel por adicionar um obj 
        no final da fila
        '''
        self.fila.append(nodo)
        return 'Item adicionado a fila com sucesso!'

    def sair_fila(self):
        '''
        Metodo responsavel por retirar
        um obj do inicio da fila
        '''
        remover = False
        if len(self.fila) > 0:
            nodo = self.fila.popleft()
            remover = True
            return f'O item {nodo.conteudo} saiu da fila!', remover
        else:
            return 'Fila está vazia, não há o que remover!', remover

    @property
    def fila(self):
        return self.__fila

    @fila.setter
    def fila(self, f):
        self.__fila = deque([])