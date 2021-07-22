# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 06:30:59 2021

@author: user
"""

import keyword
print(keyword.kwlist)
def myfun():
    a=1
    b=2
    c=a+b
x=myfun.c()
print(x)


#assert
a1=7
assert a1>10, "a is small"

# async and await
import asyncio
async def practise():
    print("hello")
    await asyncio.sleep(10)
    print("world")
asyncio.run(practise())


#break and continue
for i in range(1,6):
    if i==3:
        break
    print(i)
for i in range(3,9):
    
    if i==6:
        continue
    print(i)
    
#if elif else
def my_fun(a):
    if a==1:
        print("one")
    elif a==2:
        print("two")
    else:
        print("nothing")
my_fun(3)
my_fun(2)
my_fun(1)

#exception try raise

def reciprocal(num):
    try:
        r=1/num
    except:
        print("exception caught")
        return
    return r
reciprocal(100)
reciprocal(0)

#loops and iterations
friends=["koumudi","abhishek", "sowjanya"]
for i in friends:
    print("Hello", i, "padukundhi chalu leyandi inka")
    
#lambda function
x=lambda x:x*2
for i in range(1,5):
    print(x(i))
    
a=5.0+4j
print(a)
type(a)
b=[1,2]
b.append(3)
b
print(list("vishnu"))
a=[[1,2],[3,4]]
type(a)
print(dict(a))
type(a)


#typecasting, implicit conversion, explicit conversio
x=3
y=3.4
z=x+y
z
type(z)
#explicit or type conversion
x1=3
x2=float("4.5")
z1=x1+x2
z1
type(z1)

a1,a2=4,5
print("virat is {} and smith is {}".format(a1,a2))

print(id(x))
print(id(3))


#range function
for i in range(1,40,5):
    print(i)
    
#function example
def greet(name):
    print("hello", name, "good morning")
greet(["vishnu", "sachin"])  
