#-*-coding:utf-8-*-
import numpy as np
import function as func

def sigmoid(x):
    return 1/(1+np.exp(-x))
def identity_function(x):
    return  x
#################가중치 및 편향 초기화####################
def init_network():
    network={}
    #################가중치 설정#########################
    network['W1'] = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
    network['W2'] = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
    network['W3'] = np.array([[0.1,0.3],[0.2,0.4]])
    #################편향 값 설정########################
    network['b1'] = np.array([0.1,0.2,0.3])
    network['b2'] = np.array([0.1,0.2])
    network['b3'] = np.array([0.1,0.2])

    return network

def forward(network,x):
    W1,W2,W3 = network['W1'],network['W2'],network['W3']
    b1,b2,b3 = network['b1'],network['b2'],network['b3']
    a1 = np.dot(x,W1)+b1
    z1 = func.sigmoid(a1)
    print("First Output is z1 =",z1)
    a2 = np.dot(z1,W2)+b2
    z2 = func.sigmoid(a2)
    print("Second Output is z2 =",z2)
    a3 = np.dot(z2,W3)+b3
    y  = func.identity_function(a3)
    return y

network = init_network()
x=np.array([1.0,0.5])
y=forward(network,x)
print("Last Output is Y =",y)
