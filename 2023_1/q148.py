import numpy as np

valores = np.random.rand(3,4)
soma = 0
'''
[    0 1 2 3
    [0 0 0 0], -> 0
    [0 0 0 0], -> 1
    [0 0 0 0]  -> 2
]
'''
for i in range(0,3):#[0,3[ ->0,1,2
    for j in range(0,4):#[0,4[ ->0,1,2,3
        soma += valores[i,j]#soma = soma + valores[i,j]
print(valores)
print(soma)

print(valores.shape)
for i in range(0,3):#linhas
    for j in range(0,4):#colunas
        print(f'{valores[i,j]:.2f} ', end='')
    print()


