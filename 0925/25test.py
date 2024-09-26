import numpy as np

data = np.array(([1,2,3],[4,5,6]))
print(data)
print()
print('합계', sum(data))
print('합계', np.sum(data))
print('열합계', np.sum(data, axis = 0))
print('행합계', np.sum(data, axis = 1)) 
print()
print('누적합계', np.cumsum(data))

print()

print('-'*50)

#data = np.array(([1,2,3],[4,5,6]))
score = [1,2,3,4,5,6]

print(sum(score))
hap = 0
for k in score:
    hap = hap + k
    print(hap, end = ' ')


