import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[11,22],[33,44]])
print("a=\n",a)
print("b=\n",b)

c = np.concatenate([a,b],0)
print("np.concatenate([a,b],0)=\n",c)
c = np.concatenate([a,b],1)
print("np.concatenate([a,b],1)=\n",c)