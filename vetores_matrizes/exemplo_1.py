#Execute o seguinte comando para instalar a lib numpy
#pip install numpy

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

#verificando o tipo
print(type(arr))

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

arr2 = np.array(('1abcd', 2, 3, 4, 5), dtype='S')
print(type(arr2))
print(arr2.dtype)
print("-------------")
print(np.arange(4))

for i in arr2:
    print(i)

