# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 10:55:24 2021

@author: user
"""
#example
num=(1,2,3,4)
num.append(5)
#example
from bs4 import BeautifulSoup

#example
name='vishnu'
type(name)
type(int(name))

#example
def name():
    print("vishnu")
    print("vardhan")
name()
name()

#example
def details():
    name=input("Please enter your name: ")
    return name
def mai():
    age=int(input("Please enter your age: "))
    name1=details()
    print("My name is",name1, "and my age is", age)
if __name__=="__main__":
    mai()
print (True + False + False)
print(True+False+True)

#method 1
list=[1,2,3,4,7,9]
if (9 in list):
    print("element exist")
else:
    print("element didn't exist")

#method 2
list=[1,2,"vishnu","jeshwanth",4]
for i in list:
    if (i=='vishnu'):
        print("element exists")
#example
string=['vishnu', 'sachin', 'kohli']
for i in string:
    
    if i=='sachin':
        break
    print(i)
    
#example
string="Vishnu: reddy.vishnu66@gmail.com"
string1=string.split()
print("Name:", string1[0], '\n' "Email:", string1[1])

#example
name="jashwanth:Reddy"
Name=name.split(':')
print(Name)
print(type(Name))

#example
a,b=int(input("please enter two variables")).split()
print("enter first value")
print("enter second value")

#example
import time
counter=10
for i in reversed(range(counter+1)):
    if i>0:
        print(i, end='>>>')
        time.sleep(1)
    else:
        print("start")
    
