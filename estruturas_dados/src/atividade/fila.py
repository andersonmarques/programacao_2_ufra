from collections import deque
fifo = deque([])
fifo.append("Banana")
print(fifo)
fifo.append("Maçã")
fifo.append("Pera")
print(fifo)
fifo.append("Uva")
print(fifo)
fifo.popleft()
fifo.popleft()
print(fifo)
fifo.popleft()
print(fifo)




