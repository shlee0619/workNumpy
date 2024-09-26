import numpy as np

#파이썬 기본 array+range(10)
eng = np.arange(10).reshape(2,5)
print(eng)
print()


print(np.where(eng>5, 1, 0))
# 조건 5보다 크면 10,0


#조건 if대신 where 키워드
# import numpy as np
# a = np.arange(10)
# a
# array([0,1,2,3,4,5,6,7,8,9])
# np.where(a<5, a, 10*a)
# array([0,1,2,3,4,50,60,70,80,90])

