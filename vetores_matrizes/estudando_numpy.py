# 147. Elabore um algoritmo/programa que crie um vetor com 5 textos para
# guardar os nomes de pessoas. O vetor deve ser preenchido pelo usuário e ao
# final deve ser feita uma consulta com um novo nome para saber se ele está
# ou não cadastrado.

import numpy as np

vetor = np.array([], np.dtype('U25'))

print('Adicione 5 pessoas ao cadastro.')

for i in range(0, 2):
    nome = input(f'Usuário {i}: ')
    vetor = np.insert(vetor, i, nome)


consulta = input('Escreva o nome de usuário para saber se ele está no cadastro:')

print('O usuário já está cadastrado.' if consulta in vetor else 'O usuário NÃO está cadastrado.')
