# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 15:22:58 2021

@author: user
"""
import math
#nested_lists
x=[["sachin", "virat"], ["dhoni", "gilly"], ["rohit","watson"]]
x[2]
x[1][1]
for inner in x:
    for value in inner:
        print(value)

#delete function
z=1
print(z)
del(z)

""" exmple"""
a="vishnu"
b=1
print(a+str(b))


#tuples
c1=()
print(c1)
X=("VISHNU", "dhoni")
print(X)


c1={"vishnu":1}
b=c1.items()
print(b)
len(x)

x.update(c1)
b={**x,**c1}
print(b)
c1["vishnu"].append(4)
c1

f=open("list.py")

#directories
import os
os.getcwd()
os.listdir()
print(dir(locals()["__builtins__"]))

#example
name="my name is vishnu"
name.split()
for a in name:
    print(a)
