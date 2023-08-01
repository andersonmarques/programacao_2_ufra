import numpy as np
vetor = np.random.randn(15)
maior = -100000000
menor = 10000000
for i in range(0, len(vetor)):#[0,15[
    if vetor[i] > maior:
        maior = vetor[i]
    if vetor[i] < menor:
        menor = vetor[i]
print(vetor)
print(f'Maior: {maior}\nMenor: {menor}')