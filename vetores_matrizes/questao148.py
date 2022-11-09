import numpy as np
A = np.zeros((3,4))
somatorio = 0
for i in range(0, 3):
    for j in range(0, 4):
        A[i][j] = np.random.randn()
        somatorio += A[i][j]#somatorio = somatorio + A[i][j]
print(A)
print(f'Soma: {somatorio}')