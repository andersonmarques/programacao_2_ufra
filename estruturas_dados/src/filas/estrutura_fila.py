# Cria uma fila com três elementos.
from collections import deque
fila = deque([])#criando uma FILA vazia
# fila = deque(["Banana", "Maçã", "Pera"])
# print("Fila: ", fila)

# Adiciona um elemento ao final da fila.
fila.append("Banana")
fila.append("Maçã")
fila.append("Pera")
fila.append("Uva")
print("Adicionado elementos: ", fila)

# Remove o primeiro elemento adicionado à fila.
fila.popleft()
fila.popleft()
fila.popleft()
print("Removendo um elemento: ", fila)