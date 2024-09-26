import numpy as np

x = np.array( ([1,2,3,4,5]) )
print(x)
print(type(x))
print(x.shape)
print(x.dtype)
print(x.size)
print(x.ndim)
print()





y = np.array( ([1.9,2.8,3.7,4.6,5.1]) )
print(y)
print(type(y))
print(y.shape)
print(y.dtype)
print(y.size)
print(y.ndim)
print()

z = np.array(([1,2,3],[4,5,6],[7,8,9],[10,11,12]))
z = np.array(([1,2,3],[4,5,6],[7,8,9],[10,11,12]))
print(z)
np.save('C:\\Mtest\\testScore.npy', z)
print('C:/Mtest/Score.npy저장 성공했습니다')
