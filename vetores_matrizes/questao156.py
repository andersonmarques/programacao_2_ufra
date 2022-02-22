import numpy as np

def print_matriz(M):
    for i in range(0, len(M)):
        for j in range(0, len(M)):
            if j == len(M[0]) - 1:
                print(f'{M[i][j]}', end='')
            else:
                print(f'{M[i][j]}\t', end='')
        print('')

A = np.zeros((4,4), dtype= int)
B = np.zeros((4,4), dtype= int)

for i in range(0, len(A)):
    for j in range(0, len(A)):
        A[i][j] = (2 * i) - (3 * j)
        B[i][j] = (3 * i) - (j ** 2)
        


