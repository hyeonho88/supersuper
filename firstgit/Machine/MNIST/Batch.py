
import numpy as np
import sys
sys.path.append("c:/Users/hunho/OneDrive/문서/GitHub/supersuper/firstgit/Machine")
import function as func


x, t = func.get_data()
network = func.init_network()
W1, W2, W3 = network['W1'],network['W2'],network['W3']

print("X Shape :",x.shape)
print("X[0] Shape :",x[0].shape)
print("W1 Shape :",W1.shape)
print("W2 Shape :",W2.shape)
print("W3 Shape :",W3.shape)

batch_size = 100
accuracy_cnt = 0

for i in range(0, len(x),batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = func.predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt += np.sum(p==t[i:i+batch_size])

print("Accuracy :"+str(float(accuracy_cnt)/len(x)))
