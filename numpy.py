# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 10:30:52 2021

@author: user
'"""

import numpy as np
a=np.arange(15).reshape(3,5)
a
a.ndim
a.shape
a.dtype
b=np.arange(1,16,4).reshape(2,2)
b
c=np.zeros((2,4))
c
d=np.ones((3,4))
d
e=np.ones((2,2,2))
e
e.ndim
x=np.arange(0,10,2)
y=np.arange(5)
xy=np.vstack([x,y])
xy
set(xy)

#pract
a=np.array([1,2,3])
a.ndim
a=np.array([[[1,2],[2,3],[3,4]]])
a.ndim
a=np.array([1,2,3])
a
print(a)
a1=np.linspace(0,10,num=5)
b1=a1.linspace(num=5)
a1
c1=np.ones((1))
c1
b1=np.array([1,3,2,4,6,5,7,8])
set(b1)
np.sort(b1)
a=np.arange(5)
b=np.arange(7,11)
np.concatenate((a,b))
a=np.array([[1,2],[3,4]])
b=np.array([[4,5]])
np.concatenate((a,b), axis=1)
b.size
a.size
a.shape
a1=np.array([[1,2,3], [5,3,2]])
print(a1[a1<5])
b=np.nonzero(a1<5)
print(b)
zipped=list(zip(b[0],b[1]))
for cor in zipped:
    print(cor)

rng=np.random.default_rng(1)
rng.random(4)

#pandas
import pandas as pd
for i in range(10):
    a=pd.Series(i)
    print(a)


df
df['sum']=df['A']+df['B']
df
import random
random.randrange(1,3)
