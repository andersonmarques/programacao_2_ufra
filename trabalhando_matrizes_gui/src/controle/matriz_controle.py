import numpy as np

class Matriz_controle:
    # def __init__(self) -> None:
    #     pass
    def somar_diagonal_principal(self, M: np.ndarray):
        #algoritmo para calcular a diag principal
        soma = 0
        # M = np.array([[1,2,3],[4,5,6],[7,8,9]])
        for i in range(0, len(M)):
            for j in range(0, len(M[0])):
                if i == j:
                    soma += M[i][j]
        return soma

    def montar_matriz_usuario(self, matriz: str) -> np.ndarray:
        linhas = matriz.splitlines()#matriz.split('\n')
        M = []
        N = []
        for i in range(0, len(linhas)):
            for j in range(0, len(linhas[0])):
                N = linhas[i].split()
            M.append(N)

        M_int = np.zeros((len(M),len(M[0])))
        for i in range(0, len(M)):
            for j in range(0, len(M[0])):
                M_int[i][j] = int(M[i][j])
        
        return np.array(M_int)


