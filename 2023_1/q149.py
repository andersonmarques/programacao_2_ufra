import numpy as np

def imprimir_matriz(mat_A):
    '''Função responsavel por receber e imprimir uma matriz'''
    print("------------")
    # print(len(mat_A[0]))= 6 (quantidade de elem da linha 0)
    # print(len(mat_A)) = 3 (quant de linhas)
    for linha in range(0, len(mat_A)):
        for coluna in range(0, len(mat_A[0])):
            print("{:.2f}".format(mat_A[linha,coluna]), end=" ")
        print()

matriz = np.full((3,6), 0.)

for linha in range(0, 3):
    for coluna in range(0, 6):
        num_aleatorio = np.random.uniform(-100, 100)
        matriz[linha,coluna] = "{:.2f}".format(num_aleatorio)

print("Matriz_3,6:")
imprimir_matriz(matriz)

valor = float(input("Insira um número real para multiplicar aos elementos da matriz: "))
for linha in range(0, 3):
    for coluna in range(0, 6):
        matriz[linha,coluna] *= valor #matriz[linha,coluna] = matriz[linha,coluna] * valor

print("Valores atualizados da Matriz_3,6:")
imprimir_matriz(matriz)

