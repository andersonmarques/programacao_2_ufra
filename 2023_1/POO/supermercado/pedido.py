from item import Item
from typing import List

class Pedido:
    def __init__(self, forma_pagamento: str):
        self.lista_item: List[Item] = []
        self.forma_pagamento: str = forma_pagamento
        #forma de pagamento:
        # 1 - Dinheiro
        # 2 - Cartão de Crédito
        # 3 - Cartão de Débito
        # 4 - Cheque
        # 5 - Vale Alimentação
        # 6 - Vale Refeição
        # 7 - Vale Transporte
        # 8 - Outros