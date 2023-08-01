from produto import Produto

class Item:
    def __init__(self, produto: Produto, quantidade: int) -> None:
        self.produto: Produto = produto
        self.quantidade: int = quantidade