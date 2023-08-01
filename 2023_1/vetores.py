import numpy as np

lista = [10,15,20,25,30,35,40,45,50]#unidimencional
vetor = np.array(lista)
print(vetor)
vetor_nulo = np.zeros(10)
print(vetor_nulo)
vetor_um = np.ones(10)
print(vetor_um)
vetor_dois = np.full(10,2)
print(vetor_dois)


lista_de_lista = [
                    [1,2],
                    [3,4]
                ]
matriz = np.array(lista_de_lista)
print(matriz)
matriz_nula = np.zeros((3,3))
print(matriz_nula)#win + R

