import numpy as np

a = np.arange(1,11)
print(a)
print('합계', sum(a))
print('합계', np.sum(a))
print('합계', np.add.reduce(a))

print()

