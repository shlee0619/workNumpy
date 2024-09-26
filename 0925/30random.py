import numpy as np
import math

b = np.random.randint(1,45,10)
print(b)
c = np.random.randint(1,45,10)
print(c)

a = np.random.uniform(1,45,10)
print(a)
print('-'*100)


d = np.random.rand(10)
print(d)
print('-'*100)
x = np.random.rand(5)
print(x)
print()
print('-'*100)

y = np.random.rand(15).reshape(3,5)
print(y)
print()

z = np.random.randn(15).reshape(3,5)
print(z)
print('0.000~0.9999범위를 벗어남')

#-------------------------------------------------------------------------
print()
my = np.random.randint(1,101,500)
print(my)
print()
print('빈도수', np.bincount(my))
print('빈도수', np.bincount(my).argmax())

np.random.seed(0)
print('-'*50)
a = np.random.uniform(1,45,40) #1~45사이 실수 30개 발생
print(a)
print()
