import numpy as np
import matplotlib.pylab as plt

def numerical_diff(f,x):
    h = 1e-4
    return (f(x+h)-f(x-h))/(2*h)

def function_1(x):
    return 0.01*x**2 + 0.1*x

x=np.arange(0.0,20.0,0.1)
y=function_1(x)
'''plt.xlabel('X')
plt.ylabel('f(x)')
plt.plot(x,y)
plt.show()
'''
print(numerical_diff(function_1,5))
print(numerical_diff(function_1,10))

x0=3
x1=4

def function_tmp1(x0):
    return x0*x0 + 4.0**2
def function_tmp2(x1):
    return x1*x1 + 3.0**2


print(numerical_diff(function_tmp1,3.0))
print(numerical_diff(function_tmp2,4.0))
