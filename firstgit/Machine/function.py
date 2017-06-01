import numpy as np
import pickle
import sys
sys.path.append("c:/Users/hunho/OneDrive/문서/GitHub/supersuper/firstgit/Machine/MNIST")
import mnist as mn

def sigmoid(x):
    return 1/(1+np.exp(-x))

def identity_function(x):
    return  x

def softmax_function(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

def get_data():
    (x_train,t_train), (x_test,t_test) = \
    mn.load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open("c:/Users/hunho/OneDrive/문서/GitHub/supersuper/firstgit/Machine/MNIST/sample_weight.pkl",'rb') as f:
        network = pickle.load(f)

    return network

def predict(network, x):
    W1,W2,W3 = network['W1'],network['W2'],network['W3']
    b1,b2,b3 = network['b1'],network['b2'],network['b3']

    a1 = np.dot(x,W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1,W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2,W3) + b3
    y = softmax_function(a3)

    return y
