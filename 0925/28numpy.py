import numpy as np
import math

a = np.zeros(10)
print(a)
print()
a[3]=7
print(a)
print()

#난수 np

b = np.random.randint(1,35,10)
print(b)
c = np.random.randint(1,35,10)
print(c)
print(np.intersect1d(b,c))

print('제곱근')
print('제곱근', math.sqrt(81))
print('제곱근', np.sqrt(81))
print('제곱근', np.emath.sqrt(81))

# x = np.arange(1,17).reshape(4,4)
# print(x)

y = np.arange('2024-07','2024-09', dtype = 'datetime64[D]' )
print(y)


# y = np.array( ([1.9,2.8,3.7,4.6,5.1]) )
# print(y)
# print(type(y))
# print(y.shape)
# print(y.dtype)
# print(y.size)
# print(y.ndim)
# print()

