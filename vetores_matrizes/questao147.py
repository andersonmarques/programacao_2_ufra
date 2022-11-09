import numpy as np
v = np.zeros(5, dtype=object)
for i in range(0, len(v)):# len() retorna o tamanho do vetor
    v[i] = input(f'Digite o {i + 1}º nome:\n')
pesquisa = input('Qual o nome para a pesquisa?\n')
resultado = False
for i in range(0, len(v)):
    if pesquisa == v[i]:
        resultado = True
        break
if resultado == True:
    print(f'O nome {pesquisa} está na lista!')
else:
    print(f'O nome {pesquisa} NÃO está na lista!')