# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 15:23:10 2021

@author: user
"""

a=[1,2,3]
print(a)
a.append(4)
a
a.extend([5,6])
a
a.append([7,8])
a
a.pop()
a
a.index(4)
a.reverse()
a
import keyword
print(keyword.kwlist)

#functions greeting
def greet(*names):
    for name in names:
        print("hello", name)
greet("sachin","dhoni", "virat")

def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
num=6
print("the factorial of", num, "is",factorial(num))

#global
a=4
def fun():
    global a
    a+=2
    print(a)
fun()
dir(list)


#decimal
from decimal import Decimal as d
print(d('1.2')+d('3.4'))

#iterators
numbers=[1,2,3,4,5]
value=numbers.__iter__()
num1=value.__next__()
num2=value.__next__()
print(num1)
print(num2)

counts=[]
for i in range(1,100):
    counts.append(i)
print(counts)
count1=iter(counts)
while(True):
    try:
        count=next(count1)
        print(count)
    except StopIteration:
        break
    
def even(max):
    n=2
    while n<=max:
        yield n
        n+=2
even_numbers=even(50)
print(next(even_numbers))

count=5
while count<=10:
    print(count)
    count+=1

#multiplication table
count=1
number=int(input("Please enter the number"))
while count<=20:
    
    product=(count*number)
    print(number, "X", count, "=", product)
    count+=1


count=10
number=int(input("Please enter your number : "))
while count>=1:
    product=number*count
    print(number, "X", count, "=", product)
    count-=1

list=["vishnu", "sachin"]
for player in list:
    print("King", player, "is a great player")
number=int(input("please enter a number"))
for count in range(1,10):
    product=number*count
    print(product)


total=0
for number in range(1,51):
    total=total+number
print(total)

for count in range(1,50):
    if count==40:
        break
    print(count)

languages=["python", "java", "c", "c++"]
for i in languages:
    if i==["c","c++"]:
        continue
        print(i)
        
#functions
def greet(name,age):
    print(name)
    print(age)
greet("vishnu", 26)