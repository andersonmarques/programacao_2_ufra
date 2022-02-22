import numpy as np

def find_min(M):
    return f'{np.min(M):.4f}'

def find_max(M):
    return f'{np.max(M):.4f}'

# def find_min(M):
#     m = 100
#     p = ''
#     for i in range(0, len(M)):
#         for j in range(0, len(M)):
#             if M[i][j] < m:
#                 m = M[i][j]
#                 p = f'i:{i} j:{j}'
#     return f'{m:.4f}', p
    
# def find_max(M):
#     m = -1
#     p = ''
#     for i in range(0, len(M)):
#         for j in range(0, len(M)):
#             if M[i][j] > m:
#                 m = M[i][j]
#                 p = f'i:{i} j:{j}'
#     return f'{m:.4f}', p
   
def print_matriz(M):
    for i in range(0, len(M)):
        for j in range(0, len(M)):
            if j == len(M[0]) - 1:
                print(f'{M[i][j]:.4f}', end='')
            else:
                print(f'{M[i][j]:.4f}\t', end='')
        print('')

A = np.random.rand(4, 4) * 10

print_matriz(A)
print(f'Max: {find_max(A)}')
print(f'Min: {find_min(A)}')

