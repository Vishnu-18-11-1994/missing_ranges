# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 11:02:38 2021

@author: user
"""

def test_fun(name, age):
    print("Hello", name, "you're", age)
test_fun("vishnu", 26)
test_fun("virat", 32)

#example 2
def test_fun2(name,age=26):
    print("Hello", name, "your age is", age)
test_fun2("vishnu")
test_fun2("dhoni",40)

#exmple3
def test_fun3(name, age):
    print("my name is {0} and my age is {1}".format(name,age))
test_fun3("Vishnu", 26)

#example
def test_fun4(*args):
    for info in args:
        print(info)
test_fun4(["vishnu", 26],["sachin", 48],["dhoni",40])

#example
def test_fun5(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
test_fun5(name="vishnu", age=26)

def power(n,p):
    if p==0:
        return 1
    elif p==1:
        return n
    else:
        return n**p
power(4,2)   
power(2,4)
power(2,5)
power(3,4)

#sorting method
class sort_num:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __repr__(self):
        return str((self.a, self.b))
list=[sort_num("vishnu", 1), sort_num("sachin", 3), sort_num("dhoni",2)]
print(sorted(list, key=lambda x:x.b))

#example
class sort:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __lt__(self, obj):
        return ((self.b)< (obj.b))
    def __le__(self, obj):
        return ((self.b)<= (obj.b))
    def __gt__(self, obj):
        return ((self.b)>(obj.b))
    def __ge__(self, obj):
        return ((self.b)>=(obj.b))
    def __eq__(self, obj):
        return ((self.b)==(obj.b))
    def __repr(self):
        return str((self.a, self.b))
list1=[sort("vishnu",1), sort("virat",3), sort("dhoni", 2), sort("rohit",4)]
print(list1)
print(sorted(list1))

#example
def func(**kwargs):
    print(kwargs)
func(name="vishnu", age=26)


#example
myUniqueList=[]
def new_list(x):
    x=10
    print(x)
    print(globals()['x'])
var=new_list
var()

#example
def a():
    print("hello")
def b():
    print("hi")
    return a
var=b()
var()

#declaring type
def add(num1, num2):
    print("The first number is: ", type(num1))
    print("The second number is: ", type(num2))
    return num1+num2
add(2,3)
add(str(2), str(3))
print type(type(int))
L = ['a','b','c','d']
print("".join(L))
chr(ord('A'))
