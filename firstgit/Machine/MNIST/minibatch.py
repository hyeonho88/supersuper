#-*-coding:utf-8-*-
import sys
sys.path.append("c:/users/hunho/OneDrive/문서/GitHub/supersuper/firstgit/Machine")
import numpy as np
from mnist import load_mnist

(x_train,t_train),(x_test,t_test)=\
    load_mnist(normalize=True,one_hot_label=True)
print(x_train.shape)
print(t_train.shape)

print(np.random.choice(60000, 10))
