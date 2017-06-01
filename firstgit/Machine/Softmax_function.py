#-*-coding:utf-8-*-
import numpy as np
a = np.array([0.3,2.9,4.0])
'''
exp_a = np.exp(a) # 지수함수
print(exp_a)

sum_exp_a = np.sum(exp_a) #지수 함수의 합
print(sum_exp_a)

y = exp_a / sum_exp_a
print(y)
'''
def softmax_function(a):

    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

y = softmax_function(a)
print(y)
