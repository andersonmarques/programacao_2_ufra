from cliente import Cliente
from item import Item
from pedido import Pedido
from produto import Produto

# Criar objetos Produto
produto1 = Produto("Camiseta", 29.99, 10)
produto2 = Produto("Calça", 59.99, 5)

# Criar objetos Item
item1 = Item(produto1, 2)
item2 = Item(produto2, 1)

# Criar objeto Pedido
pedido = Pedido("Cartão de Crédito")
pedido.lista_item.append(item1)
pedido.lista_item.append(item2)

# Criar objeto Cliente
cliente = Cliente("João")
cliente.lista_pedido.append(pedido)

# Acessar atributos e realizar interações
print(f'Nome do cliente: {cliente.nome}')  

# Acessar lista de pedidos do cliente
for pedido in cliente.lista_pedido:
    print(f'Forma de pagamento: {pedido.forma_pagamento}')  
    
    # Acessar lista de itens do pedido
    for item in pedido.lista_item:
        print(f'O cliente {cliente.nome} comprou {item.quantidade} {item.produto.nome}(s)')  
