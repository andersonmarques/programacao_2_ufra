# Faça um programa para obter as matrizes A = (aij)4x4 e B = (bij)4x4,
# sabendo que suas leis de formação são 
# aij = 2i – 3j 
# bij = 3i – j**2.

import numpy as np

A = np.zeros((4,4), dtype= int)

B = np.zeros((4,4), dtype= int)

for i in range(0, len(A)):
    for j in range(0, len(A)):
        A[i, j] = (2 * i) - (3 * j)
        B[i, j] = (3 * i) - (j ** 2)
        # print(A[i, j])
        # print(B[i, j])

print(A)
print('---------')
print(B)