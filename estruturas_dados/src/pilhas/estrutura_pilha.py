#pilha = [0, 1, 2, 3, 5]
pilha = []
pilha.append(0)
pilha.append(1)
pilha.append(2)
pilha.append(3)

print("Pilha: ", pilha)
#inserir no final
pilha.append(8)
print("Inserindo um elemento: ", pilha)

pilha.append(14)
print("Inserindo outro elemento: ", pilha)
#pop vai remover do final
pilha.pop()
print("Removendo um elemento: ", pilha)

pilha.pop()
print("Removendo outro elemento: ", pilha)
pilha.pop()
pilha.pop()
print("Removendo outro elemento: ", pilha)