# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 11:33:24 2021

@author: user
"""
for x in range(6):
    print(x)
# sample
print([[x,y] for x in [1,2,3] for y in [4,5,6]])
 #other way to write
 variable=[]
 variable.append(2)
 variable.insert(0,4)
 variable.extend(2)
 variable
 for x in [1,2,3]:
     for y in [4,5,6]:
         variable.append([x,y])
variable

#2 example
multiple_two= [x for x in range(20) if x%2==0]
multiple_two

#actual problem
x=int(input())
y=int(input())
z=int(input())
n=x+y+z


print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=n])


#split and strip
x=" v i s h "
print(x.strip())
print(x.split())

a=[]
for i in range(1,10):
    a.append(i)
print(a)
from random import shuffle
x=shuffle(a)
print(x)

a=10
if a>10:
    print("a is higher")
elif a<10:
    print("a is lower")
else:
    print("a is equal")

#keywords
import keyword
print(keyword.kwlist)
print(False==0)
print(None==0)

#split sub subn
import re
name="vishnu vardhan reddy"
name.split()
name.sub('vishnu', "sachin")
help("sub")
help()
num=[]
num.append(10)
num
num.extend([11,111])
num
num.insert(1,2)
num

#functions
def getinteger():
    result=int(input("please enter the number"))
    return result
def main():
    print("start")
    output=getinteger()
    print(output)
main()

import math
count=4
def cou_c():
    global count
    count=count+1
    print(count)
cou_c()

s= 1+2+3+ \ 
    4+5+6
s
j=1
while j<5:
    print("hello")
    j=j+1
#input functions
x,y=input("enter two values").split()
print("number of boys", x)
print("number of girls", y)

a,b=input("enter number of boys and girls:").split()
print("the total number of boys is {} and the total number of girls is {}".format(a,b))
print()
import time
print("vishnu king of world and", end=(" king of cricket"))
5)
    else:
        print("start")for i in reversed(range(1,4)):
    if i>0:
        
        print(i, end='>>', flush=True)
        time.sleep(
       