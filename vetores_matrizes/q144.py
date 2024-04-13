import numpy as np
nomes = np.zeros(10, dtype='object')

for i in range(0,10):
    nomes[i]=input('Digite seu nome:\n')

for i in range(0,10):
    print(f'{i+1}º: {nomes[i]}')