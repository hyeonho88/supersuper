import numpy as np
import function as func


a = np.array([0.3,2.9,4.0])
y = func.softmax_function(a)
print(y)
print(np.sum(y))
##SoftMax 함수의 총합은 1이 되며, 출력은 0~1.0 사이 실수이다.
