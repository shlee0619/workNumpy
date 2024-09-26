import numpy as np

#파이썬 기본 array+range(16) 0~15까지 총 16개

eng = np.arange(16).reshape(4,4) #숫자발생
print(eng)

print()

my = np.array([175,177,179,181,183])
print(my)
print('분산 ', int(np.var(my)))
print('표준편차', round(np.std(my),2))
print()
print('최대', np.max(my))
print('최소', np.min(my))


print('최대위치 ', np.argmax(my))
print('최소위치 ', np.argmin(my))
