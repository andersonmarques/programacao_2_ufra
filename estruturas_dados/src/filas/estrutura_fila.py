# Cria uma fila com três elementos.
from collections import deque
fila = deque([])
# fila = deque(["Banana", "Maçã", "Pera"])
# print("Fila: ", fila)

# Adiciona um elemento ao final da fila.
fila.append("Banana")
fila.append("Maçã")
fila.append("Pera")
fila.append("Uva")
print("Adicionando um elemento: ", fila)

# Remove o primeiro elemento adicionado à fila.
fila.popleft()
fila.popleft()
fila.popleft()
fila.popleft()
print("Removendo um elemento: ", fila)