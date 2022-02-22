lista = []
lista = ['a','b','c']

#alterando posicao da lista
lista[0] = 'aa'
print(lista)

del lista[1]

print(lista)

lista.append('x')

print(lista)

lista.insert(0, 'pri')

lista.insert(2, 'd')

print(lista)
