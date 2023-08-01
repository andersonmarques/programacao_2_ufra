
class Produto:
    def __init__(self, nome: str, preco: float, quantidade_estoque: int) -> None:
        self.nome: str = nome
        self.preco: float = preco
        self.quant_estoque: int = quantidade_estoque