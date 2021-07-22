# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 12:31:04 2021

@author: user
"""

myUniqueList=[]
def my_fun(n):
    for i in range(n):
    
        c=i
        myUniqueList.append(c)
    global_variable='c' in globals()
    print(global_variable)
fruits=["apple", "banana", "mango"]
c=my_fun
my_fun(10)
c(20)

myUniqueList

#numpy
import numpy as np
a=np.empty((3,4),0, dtype=int)
print(a)
b=np.full((3,3), 23, dtype=int)
print(b)
c=np.full((3,3),0)
print(c)

#removing non numerical values
data=np.array([[1,2,3],[4,np.nan,np.nan]])
print(data)
Data=data[~np.isnan(data).any(axis=1)]
print(Data)

#example
count=np.arange(12).reshape(4,3)
count
repr(count).count("1,2")

#swapping 2 variable
x=int(input("Please enter the first number: "))
y=int(input("Please enter the second number: "))
temp=x
x=y
y=temp
print(x)
print(y)

#2nd method
x=int(input("Please enter the first number: "))
y=int(input("Please enter the second number: "))
x,y=y,x
print(x)
print(y)

#squares

def power(a,b):
    return a**b
def square(n):
    return n**2
square(2)
square(5)

#area of a triangle
def aot(a,b,c):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    return area
aot(4,5,6)
aot(5,6,7)

import random
a=random.randint(1,8)
a

#positive negative
def pos_neg(n):
    if n>0:
        print("positive")
    elif n==0:
        print("number is zero")
    else:
        print("Negative")
pos_neg(4)
pos_neg(0)
pos_neg(-5)
a=4-5
pos_neg(a)

#even or odd
def even_odd(n):
    if n%2==0:
        print("Even")
    else:
        print('Odd')
even_odd(0)
def year(n):
    if n%4==0 or n%100==0:
        print("leap Year")
    else:
        print("Not a leap year")
year(2010)
year(2012)
year(2008)
year(2016)

#largest number
def largest_number(a,b,c):
    if a > (b and c):
        print("a is greater")
    elif b > (a and c):
        print("b is greater")
    else:
        print("c is greater")
largest_number(4,6,5)
largest_number(4,3,2)
largest_number(2,3,4)

#prie number
def prime_number(n):
    if n==1:
        print("Not a Prime member")
    elif n%2 !=0 and n%n !=0:
        print("Prime member")
    else:
        print("Not a Prime")
prime_number(15)
prime_number(9)
prime_number(8)

#prime number
num=int(input("Please enter the number:"))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print("It is not a prime number")
            break
    else:
        print("it is a prime number")
else:
    
    print("Not a prime")

#factorial
def factorial(n):
    while n>2:
        return n*n-1
    n=n+1
factorial(5)


#multiplication table
def multiplication(n):
    for i in range(1, 10):
        mul=n*i
        print(n, "X", i, '=', mul)
multiplication(8)        

#fibonaci series
def fibonaci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return n== n, n-1
fibonaci(5)
2%3
2%4
4%2
6%2
6%4
6//4

#natural numbers
sum=0
if num<0:
    print("Please enter postive number")
else:
    while (num>0):
        sum+=num
        num-=1
#example
print("vishnu \n"  "vardhan")

#remove duplicate
dup=[1,2,3,4,4,5,5,7,6,5,8,7,8,8,9,4,5]
new_list=[]
for i in dup:
    if i not in new_list:
        new_list.append(i)
new_list

#another method
from collections import OrderedDict
new=list(OrderedDict.fromkeys(dup))

#occurence of characters
count=0
name="vishnu vardhan reddy"
character='v'
for i in name:
    if i==character:
        count+=1
print(count)

name.count('v')

#timer
import time
def count_down(x):
    while x:
        min,sec=divmod(x, 60)
        timeformat="{:02d}:{:02d}".format(min,sec)
        print(timeformat, end='\r')
        time.sleep(1)
        x-=1
    print("Stop")
count_down(int(10))

#example
name="vishnu", "sachin"
print(' '.join(name))

#permutations
from itertools import permutations
words=[''.join(p) for p in permutations('vishnu')]
print(words)

import pathlib
print(pathlib().Path().absolute())

import os
os.getcwd()

number=12345678
a=str(number)[::-1]
print(a)
