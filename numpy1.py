#1
import numpy as np
n = np.random.random((10,1))
print(n)
print(np.mean(n, dtype=np.float64))

#2
import numpy as np
n = np.random.random((20,1))
print(n)
print(np.var(n))
print(np.std(n))

#3
import numpy as np
a = np.random.random((10,20))
b = np.random.random((20,25))
print(a)
print("\n")
print(b)
print("\n")

n = np.matmul(a,b)
print(n)
print("\n")

print(np.sum(n))


#4
import  numpy as np
import math
n = np.random.random((10,1))
m=[]
print(n)

for i in range(10):
    x=1/(1+math.exp(-n[i]))
    m.append(x)
print(m)

