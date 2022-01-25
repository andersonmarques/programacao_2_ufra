
class Nodo:

    def __init__(self) -> None:
        self.conteudo = None
        self.msg = ''

    @property
    def conteudo(self): #get -> recuperar dado
        return self.__conteudo

    @conteudo.setter #set -> modificar dado
    def conteudo(self, c):
        if c != None and len(c) != 0:#entao o usuario digitou algo
            self.__conteudo = c
        else:
            self.msg = 'O conteúdo do item é obrigatório!'

    