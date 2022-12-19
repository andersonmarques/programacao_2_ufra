from model.matriz import Matriz
from util.voz import Voz
from math import pow


class Matriz_controle:
    
    def __init__(self) -> None:
        self.erro = ""
        self.__voz = Voz()

    def somar_diagonal_principal(self, M: Matriz) -> float:
        '''
        Algoritmo para calcular a diag principal
        '''
        soma = 0
        if M.is_quadrada():
            for i in range(0, len(M.valores)):
                for j in range(0, len(M.valores[0])):
                    if i == j:
                        soma += M.valores[i][j]            
        else:
            self.erro = 'A matriz não é quadrada.'
        
        return soma

    def somar_diagonal_secundaria(self, M: Matriz) -> float:
        '''
        Algoritmo para calcular a diag secundaria
        '''
        soma = 0
        if M.is_quadrada():
            for i in range(0, len(M.valores)):
                for j in range(0, len(M.valores[0])):
                    if (i + j) == (M.linha - 1):
                        soma += M.valores[i][j]            
        else:
            self.erro = 'A matriz não é quadrada.'
        
        return soma

    def calcular_elemento_matriz_produto(self, ele_m, ele_n, A: Matriz, B: Matriz) -> float:
        '''
        Algoritmo para calcular um dado elemento da matriz produto
        '''
        soma = 0
        if A.coluna == B.linha:
            for t in range(0, A.coluna):
                soma += A.valores[ele_m][t] * B.valores[t][ele_n]            
        else:
            self.erro = "A.coluna é diferente de B.linha."

        return soma

    def subtrair_matrizes(self, A: Matriz, B: Matriz) -> Matriz:
        '''
        Método para calcular a soma entre duas matrizes quadradas
        '''
        C = Matriz(A.linha, A.coluna)
        if A.mesma_ordem(B):
            for i in range(0, len(C.valores)):
                for j in range(0, len(C.valores[0])):
                    C.valores[i][j] = A.valores[i][j] - B.valores[i][j]
        else:
            if not A.erro_matriz:
                self.erro = 'Erro! As matrizes não possuem a mesma ordem!'
            else:
                self.erro = A.erro_matriz
        return C

    def somar_matrizes(self, A: Matriz, B: Matriz) -> Matriz:
        '''
        Método para calcular a soma entre duas matrizes quadradas
        '''
        C = Matriz(A.linha, A.coluna)
        if A.mesma_ordem(B):
            for i in range(0, len(C.valores)):
                for j in range(0, len(C.valores[0])):
                    C.valores[i][j] = A.valores[i][j] + B.valores[i][j]
        else:
            if not A.erro_matriz:
                self.erro = 'Que pena! mas as matrizes não possuem a mesma ordem!'
            else:
                self.erro = A.erro_matriz
        return C

    def transpor_matriz(self, B: Matriz) -> Matriz:
        B_t = Matriz(m = B.coluna, n = B.linha)
        for i in range(0, B.linha):
            for j in range(0, B.coluna):
                B_t.valores[j][i] = B.valores[i][j]
        
        return B_t

    def multiplicar_matrizes(self, A: Matriz, B: Matriz) -> Matriz:
        resultado = Matriz(A.linha, B.coluna)
        if A.coluna == B.linha:
            for i in range(0, A.linha):
                for j in range(0, B.coluna):
                    for t in range(0, A.coluna):
                        resultado.valores[i][j] += A.valores[i][t] * B.valores[t][j]            
        else:
            self.erro = "Que pena! Mas coluna de A é diferente de linha de B."
        
        return resultado

    def converter_texto_para_matriz(self, matriz: str) -> Matriz:
        '''
        Converte o texto do usuario, que está no formato de matriz, em um obj Matriz
        '''
        linhas = matriz.splitlines()#matriz.split('\n')
        M = []
        N = []
        for i in range(0, len(linhas)):
            #for j in range(0, len(linhas[0])):
            N = linhas[i].split()
            M.append(N)
        
        new_matriz = Matriz(m = len(M), n = len(M[0]))
        new_matriz.valores = M

        return new_matriz
    
    def calcular_determinante(self, d: Matriz) -> float:
            det = 0;
            if d.ordem() == 1: 
                det = d.valores[0][0]
            elif d.ordem() == 2:            
                det = self.calcular_det_seg_ordem(d)
            elif d.ordem() >= 3:
                det = self.calcular_det_laplace(d)
            else:
                self.erro = 'Que Pena! Mas a matriz não é quadrada!'
            return det

    def calcular_det_laplace(self, x: Matriz) -> float:
        '''
        Metodo que calcula o determinante de uma matriz de ordem n >= 3 uitilizando o teorema de Laplace.
        Este metodo faz as chamadas ao calculo do cofator considerando sempre a primeira linha da matriz
        '''
        det = 0
        for posicao_j in range(0, x.ordem()):
            submatriz = self.gerar_submatriz(0, posicao_j, x)
            if x.valores[0][posicao_j] != 0:
                cof = self.calcular_cofator(0, posicao_j, submatriz)#posicao_j = linha + coluna -> sempre considero a linha 0, logo posicao_j = coluna
                det += cof * x.valores[0][posicao_j]
                
        return det;

    def gerar_submatriz(self, i, j, original: Matriz) -> Matriz:
        submatriz = Matriz(original.ordem() - 1, original.ordem() - 1)
        col_aux = 0
        
        for linha in range(0, original.ordem()):             
            for coluna in range(0, original.ordem()): 
                if i != linha and j != coluna:
                        submatriz.valores[linha - 1][col_aux] = original.valores[linha][coluna]
                        col_aux += 1
            col_aux = 0
            
        return submatriz

    def calcular_cofator(self, i: int, j: int, x: Matriz) -> float:
        '''
        Metodo para calcula o cofator de um elemento A[i,j]
        @param expoente soma de i + j
        @param x Determinante da matriz que se obtem de A eliminando-se a linha i e coluna j
        @return O numero que representa o cofator do elemento Aij
        '''
        expoente = i + j
        cof = int(pow((-1), expoente) * self.calcular_determinante(x))
        return cof

    def calcular_det_seg_ordem(self, d: Matriz) -> float:
        '''
        Metodo para calcular um determinante de uma matriz de segunda ordem
        '''
        diagonalPrincipal = 1;
        diagonalSecundaria = 1;
        for i in range(0, d.linha):
            for j in range(0, d.linha): 
                if i == j :
                    diagonalPrincipal *= d.valores[i][j];#produto da diagonal principal
                if (i + j) == (d.linha - 1):
                    diagonalSecundaria *= d.valores[i][j];#produto da diagonal secundaria
        
        return diagonalPrincipal - diagonalSecundaria;
        
    def falar_mensagem(self, msg: str):
        self.__voz.falar_msg(msg)

    def metodo_hungaro(self, M: Matriz) -> Matriz:
        '''Método hungaro: algoritmo de otimização de matrizes'''
        
        self.erro = ''
        if M.is_quadrada():        
            M = self.hungaro_passo1(M)
            M = self.hungaro_passo2(M)
            self.hungaro_passo3(M)
        else:
            self.erro = "A matriz não é quadrada!"
        
        return M

    def hungaro_passo1(self, M: Matriz) -> Matriz:
        '''
        Subtrair a menor entrada em cada linha de todas as entradas desta linha
        '''
        menor_l = Matriz(M.linha, 1)
        for i in range(0, M.linha):
            menor = M.valores[i][0]
            for j in range(0, M.coluna):
                if M.valores[i][j] <= menor:
                    menor = menor_l.valores[i][0] = M.valores[i][j]
            
        for i in range(0, M.linha):
            for j in range(0, M.coluna):
                M.valores[i][j] = M.valores[i][j] - menor_l.valores[i][0]
        
        return M

    def hungaro_passo2(self, M) -> Matriz:
        '''
        Subtrair a menor entrada em cada coluna de todas as entradas desta coluna.
        Esse passo será execultado somente nas colunas que não apresentem zero.
        '''
        menor_c = Matriz(1, M.coluna)
        for j in range(0, M.coluna):
            menor = M.valores[0][j]
            for i in range(0, M.linha):
                if M.valores[i][j] == 0:
                    menor_c.valores[0][j] = 0
                    break
                elif M.valores[i][j] <= menor:
                    menor = menor_c.valores[0][j] = M.valores[i][j]

        for j in range(0, M.coluna):
            for i in range(0, M.linha):
                M.valores[i][j] = M.valores[i][j] - menor_c.valores[0][j]

        return M

    def hungaro_passo3(self, M: Matriz):
        '''
        Traçar “retas” sobre as lin e col que contenham zeros, de tal forma que um número mínimo de retas horizontais 
        e verticais sejam utilizadas.
        '''
        #self.gerar_submatriz(0,0,M)
        matriz_linha = Matriz(1, M.coluna)
        matriz_coluna = Matriz(M.linha, 1)
        id_zeros = Matriz(M.linha, M.coluna)

        for i in range(0, M.linha):
            for j in range(0, M.coluna):
                if M.valores[i][j] == 0:
                    id_zeros.valores[i][j] = True
                else:
                    id_zeros.valores[i][j] = False
        incio_j = 0
        for i in range(0, M.linha):   
            # i_tem_zero = self.contem_zero(M.valores[i,:])
            for j in range(incio_j, M.coluna):
                if M.valores[i][j] == 0:
                    print(f'leu ate a coluna {j}')
                    #tentar ler o j ao contrario
                    matriz_coluna.valores[i][0] = self.calcular_somatorio(M.valores[i,-j])
                    matriz_linha.valores[0][j] = self.calcular_somatorio(M.valores[:,j])#toda coluna j
                    incio_j += 1
                    break
                else:
                    continue

    def calcular_somatorio(self, vetor):
        '''Calcular o somatorio de todos os elementos de uma matriz M'''
        soma = 0
        for i in range(0, len(vetor)):
            soma += vetor[i]
        return soma

    def contem_zero(self, vetor):
        contem = False
        for i in range(0, len(vetor)):
            if vetor[i] == 0:
                contem = True
                break
        return contem

    ########### Propriedades ###############
    @property
    def erro(self):
        return self.__erro

    @erro.setter
    def erro(self, erro_msg):
        self.__erro = erro_msg

