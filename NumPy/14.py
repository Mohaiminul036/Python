import numpy as np
import copy

a = [[x+y for x in range(5)] for y in range(6)]
a = np.array(a).astype(int)

b = copy.deepcopy(a[0::3,::2])
b[1][1] = 99
print(a)