import numpy as np
import function as func

a = np.array([1010,1000,990])
y=func.softmax_function(a)
print(y)

##최대 값 설정##
c = np.max(a)
print(a-c)

y = np.exp(a-c) / np.sum(np.exp(a-c))
print(y)
