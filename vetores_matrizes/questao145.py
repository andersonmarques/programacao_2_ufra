#pip install numpy
import numpy as np
vetor_x = np.zeros(10)
n = len(vetor_x)#len() retornar o tamanho do vetor
print(type(vetor_x))
somatoria = 0
for i in range(0, n):#[0,9[->0,1,2,3,4,5,6,7,8,9
    vetor_x[i] = int(input('Digite um valor inteiro:\n'))
    somatoria += vetor_x[i]
media = somatoria / n

for i in range(0, n):
    if vetor_x[i] > media:
        print(f'-> {vetor_x[i]}')