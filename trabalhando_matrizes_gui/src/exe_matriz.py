from entidades.matriz import Matriz

A = Matriz(2, 3)
print('-----------')
print(A.linha)
print(A.coluna)
print(A.valores)
print('-----------')
A.linha = 3
A.coluna = -4
print(A.linha)
print(A.coluna)
print(A.criar_matriz_nula())
