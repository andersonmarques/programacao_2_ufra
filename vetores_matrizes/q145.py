import numpy as np
num = np.zeros(10, dtype='int')
soma = 0
for i in range(0,10):
    num[i]=int(input(f'Digite o {i+1}º valor:\n'))
    soma += num[i]
media = soma / len(num)
# media = np.mean(num)
print(media)
for i in range(0,10):
    if num[i] > media:
        print(f'{i+1}º: {num[i]}')