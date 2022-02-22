fifo = []
fifo = ['a','b','c']
fifo[0] = 'aa'
print(fifo)
del fifo[1]
print(fifo)
fifo.append('x')
print(fifo)
fifo.insert(0, 'pri')
fifo.insert(2, 'd')
print(fifo)