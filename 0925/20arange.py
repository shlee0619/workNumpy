import numpy as np

kor = np.arange(0,16).reshape(4,4)

print(kor)
print()

eng = np.arange(0,16).reshape(4,4)
print(eng)


print('대각합계', np.trace(eng))

mat_3d = np.arange(0,27).reshape(3,3,3) #3면 3행 3열
print(mat_3d)
print()
print(np.trace(mat_3d))
