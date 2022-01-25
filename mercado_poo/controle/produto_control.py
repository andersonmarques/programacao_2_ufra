from entidades.produto import Produto

class Produto_Control:

    def __init__(self) -> None:
        self.lista_produtos = None

    def salvar_produto(self, produto):
        self.lista_produtos.append(produto)

        return 'Produto salvo com sucesso!'

    @property
    def lista_produtos(self):
        return self.__lista_produtos

    @lista_produtos.setter
    def lista_produtos(self, lista):
        self.__lista_produtos = []

    
