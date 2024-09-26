import numpy as np



#파이썬 기본 range(7) range(1,7) range(1,7,1)
kor = np.arange(1,16).reshape(5,3)

print(kor)
print()

eng = np.arange(0,16).reshape(4,4)
print(eng)


print('대각합계', np.trace(eng))

mat_3d = np.arange(0,27).reshape(3,3,3) #3면 3행 3열
print(mat_3d)
print()
print(np.trace(mat_3d))

com_3d = np.arange(27).reshape(3,3,3)
print(com_3d)
