from pedido import Pedido
from typing import List

class Cliente:
    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.lista_pedido: List[Pedido] = []
