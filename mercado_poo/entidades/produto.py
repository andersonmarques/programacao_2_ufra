import re


class Produto:

    def __init__(self, nome = None, codigo = None, preco = None, quant_estoque = None) -> None:
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.quant_estoque = quant_estoque
        self.erro_validacao = ''

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if nome != None and len(nome) != 0:
            self.__nome = nome
        else:
            self.erro_validacao = 'O campo "nome" é obrigatório!'

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if codigo != None and len(codigo) != 0:
            self.__codigo = codigo
        else:
            self.erro_validacao = 'O campo "Código" é obrigatório!'

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        if preco != None and len(preco) != 0:
            self.__preco = float(preco)
        else:
            self.erro_validacao = 'O campo "Preço" é obrigatório!'

    @property
    def quant_estoque(self):
        return self.__quant_estoque

    @quant_estoque.setter
    def quant_estoque(self, quant):
        if quant != None and len(quant) != 0:
            self.__quant_estoque = int(quant)
        else:
            self.erro_validacao = 'O campo "Quant. do estoque" é obrigatório!'