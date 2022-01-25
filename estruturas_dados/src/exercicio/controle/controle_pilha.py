
class Controle_Pilha:
    def __init__(self) -> None:
        self.pilha = None

    def empilhar(self, nodo):
        self.pilha.append(nodo)
        return 'Item empilhado com sucesso!'

    def desempilhar(self):
        removeu = False
        if len(self.pilha) > 0:
            self.pilha.pop()
            removeu = True
            return 'Item desempilhado com sucesso!', removeu
        else:
            return 'Pilha vazia!', removeu

    @property
    def pilha(self):
        return self.__pilha

    @pilha.setter
    def pilha(self, p):
        self.__pilha = []