# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 13:22:03 2021

@author: user
"""

import numpy as np
arr=np.array([1,2,3])
print(arr)
tup=np.array((1,4,5))
print(tup)
type(tup)
type(arr)
d=np.array([[1,2,3],[4,5,6]])
print(d)
type(d)
for i in range(1,9):
    print(np.array(i))

# array with slicing removing columns and rows
arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
arr
arr1=arr[:3, ::2]
arr1
#elements at indices
arr2=arr[[1,2,0,0],[2,2,1,0]]
print(arr2) 

#basic operations
arr3=np.array([[1,2,3],[4,5,6]])
print(arr3+1)
print(arr3-1)
print(arr3*2)
arr4=np.array([[4,5,6],[7,8,9]])
arr3+arr4
arr3*arr4
arr3.sum()
arr4.sum()
arr.dtype
arr.T
arr.size
arr.dtype
arr.ndim
arr.shape
arr5=np.array([[1,2,3],[4,5,6]], dtype='float')
arr5
arr6=np.array([1,2,3], dtype='int')
arr6
arr7=np.zeros((3,4), dtype='int')
arr7
arr8=np.ones((3,4))
arr8
arr9=np.full((3,4),6, dtype='complex')
arr9
arr
arr.min()
arr.max()
print(arr.min(axis=1))
arr.cumsum(axis=1)
arr=np.array([[1,2],[3,4]])
arr2=np.array([[2,4],[5,6]])
arr.dot(arr2)
arr2.dot(arr)

#arrays
import array
arr=array.array('i',[1,2,3])
arr
for i in range(0,3):
    print()

#array
a=np.empty(2,dtype=int)
a
a=np.empty([2,2], dtype=int)
a
b=np.empty([4,5], dtype=int)
b
c=np.empty([3,3],dtype=int)
c
d=np.arange(8).reshape(2,4)
d
c=np.arange(6)
c
e=np.arange(18).reshape(3,2,3)
e

list1=[1,2,3,4]
list2=[5,6,7,8]
a=np.array(list1)
b=np.array(list2)
print(a*b)

#arrays
a=np.arange(10,1,-2)
a
na=a[np.array([3,4])]
na
b=np.arange(8).reshape(2,4)
b
for x in np.nditer(b):
    print(x)

b=np.arange(0,100,10).reshape(5,2)
b
for x in np.nditer(b):
    print(x)
    
    
#numpy strings
import numpy as np
a=np.char.lower(["VISHNU","VARDHAN"])
a
b=np.char.lower(("VISHNU","VARDHAN"))
b
name="vishnu vardhan reddy"
name
b=np.strip(name)
name.strip()
name.capitalize()
name.center(30, '*')
name.upper()
name.lower()
name.split()
name.encode()
name.decode()
name.ljust(25)
name.rjust(25)

#sorting
sort1=np.array([[2,4],[1,3]])
sort1
sort2=np.sort(sort1, axis=1)
sort2

sort3=np.array([4,3,5,2,6,7,9,1,8])
sort3
sort4=np.sort(sort3)
sort4
np.argsort(sort4)
sort6=np.array([1,2,3,5,4,6,7,8])
np.argsort(sort6)

#pandas
import pandas as pd
for i in range(1,11):
    print(pd.Series(i))

list=["geeks", "for", "geeks"]
list1=pd.DataFrame(list)
list1

#dataset
import pandas as pd
data=pd.read_csv("C:\\Users\\user\\Downloads\\nba.csv", index_col='Name')
data
data.info()
data.describe()
first=data.loc['Avery Bradley']
second=data.loc['Markel Brown']
print(first,"\n\n", second)
age=data['Age']
height=data.iloc[17]
height
data.isnull()
data.fillna(0)

#matplot
import matplotlib.pyplot as plt
a=[1,2,3,4]
b=[5,6,7,8]
plt.plot(a,b)
plt.title("simple graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#re
import re
a=re.compile("[a-e]")
print(a)
print(a.findall("vishnu vardhan reddy"))
