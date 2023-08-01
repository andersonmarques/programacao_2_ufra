import numpy as np

nomes = np.zeros(10, dtype=object)

for i in range(0, 10):#[0,10[
    nomes[i] = input('Entre com um nome:\n')

for i in range(0,10):
    print(f'{i+1}ª posição: {nomes[i]}')
    