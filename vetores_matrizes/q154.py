import numpy as np

matriz = np.random.rand(3,6)

soma_vendas = 0
valor_vendedor_top = 0
vendedor_top = ""

for i in range(0, len(matriz)):
    for j in range(0, len(matriz[0])):
        soma_vendas += matriz[i][j]

        soma_vendedor = 0
        soma_vendedor += matriz[i][j]
        print(soma_vendedor)
        if soma_vendedor >= valor_vendedor_top:
            vendedor_top = f"Vendedor {i+1}"

print(np.round(matriz,2))
print('Soma de vendas: {:.2f}'.format(soma_vendas))
print(f'Vendedor top: {vendedor_top}')