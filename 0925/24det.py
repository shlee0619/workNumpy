import numpy as np

# 접근 np.random.rand()
# 접근 np.linalg.det()

a = np.array([[1,2],[3,4]])
print(a)

#값 = 1*4-2*3

ret = np.linalg.det(a)
print('np.linalg.det ', ret)
print('소숫점~.det', round(ret,2))
print('절대값~.det', np.abs(ret))

b = np.array([[1,2],[3,4]])
print(b)
print()
#ret = np.linalg.det(b)
ret = np.linalg.inv(b)
print(ret)

print(b*ret)
print(np.round(np.dot(b,ret), decimals=10))
'''
원본 [[1 2] [3 4]]
     4  3  / 2  1
결과 [[-2. 1.] [1.5 -0.5]]

'''

print()