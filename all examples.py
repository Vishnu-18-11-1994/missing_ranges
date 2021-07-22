# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 09:34:18 2021

@author: user
"""

name=["vishnu", "vardhan", "reddy"]
print("g", "j", sep="")
import time
timer=5
for i in reversed(range(timer+1)):
    if i>0:
        print(i, end='<<<', flush=True)
        time.sleep(1)
    else:
        print("started")

a=[1,2,3,4]
print(a)
name="vishnu"
lastname="nagasani"
print(name, lastname)

import antigravity
name="vishnu"
print(name.center(20,'#'))
print(name.ljust(10,"-"))
4/2
4//2
8/3
8//3
8%4
8%5
2**3
4**2
a=3
b=3
a>b
a<b
a==b
a!=b
a>=b
a<=b
a=[1,2,3]
b=[1,2,3]
a==b
a is b

list1=[]
for i in range(1,10):
    list1.append(4*i)
    print(i)
print(list1)

import operator
a=1
b=2
print("The addition of 2 numbers is", operator.add(a,b))
operator.gt(a,b)
print(int(a) in int(b))

str1="geeks for geeks"
for i in reversed(range(str1)):
    print(i)
print("hello", end=" ")
print(str1)
print(len(str1))
print(str1[5])

#lists
list2=[[1,2,3],[4,5,6]]
type(list2)
len(list1)
list3=[1,2,3,2,3,2,4,5,4,5,6,7,6,7]
print(list(set(list3)))

#list comprehension
odd_square=[x**2 for x in range(1,20) if x%2==1]
print(odd_square)

#sets
set1="vishnu vardhan reddy"
print(set(set1))

#dictionary
name=dict([(1,2), ("vishnu",1)])
print(name)


#number guessing game
import random
import math
lower=int(input("please enter lower number: "))
upper=int(input("please enter upper number: "))
x=random.randint(lower,upper)
print("you have", round(math.log(upper-lower+1,2)),"chances")
count=0
while count<=round(math.log(upper-lower+1,2)):
    count+=1
    guess=int(input("please enter your number: "))
    if x==guess:
        print("you guessed it in", count, "try")
        break
    elif x>guess:
        print("you guessed it low")
    elif x<guess:
        print("you guessed it high")
if count>round(math.log(upper-lower+1,2)):
    print("The number is", x)
    print("Better luck next time")

#hangman game
words="my name is vishnu vardhan reddy and i am the king of the world"    
words.split()
word=random.choice(words)    
word

#dictionary
d=dict()
d['x']=1
d['y']=2
for i in d:
    print(i, d[i])

#example
sum=0
for i in range(1,11):
    sum=sum+i
    
        
    print(sum)
print(sum)

for key, value in enumerate(["vishnu", "vardhan", "reddy"]):
    print(value,key)
    
#example
question=["Team", "How do they play in league matches", "what about knockouts"]
answer=["India", "wins almost every match", "chokes everytime"]
for question, answer in zip(question,answer):
    print(question,":",answer)

#iter
cricket={"Dhoni":"Captain Cool", "Virat":"Fire", "Williamson":"Ice"}
for key,value in cricket.items():
    print(key,":", value)
    
#function
def even(x):
    if x%2==0:
        print("even")
    else:
        print("odd")
even(1)

#2
def intro():
    "Hello vishnu what's up"
print(intro.__doc__)

#example
def myfun(x):
    x=[1,2,3]
    
lst=[6,7,8,9]
myfun(lst)
print(lst)

#swap
def swap(x,y):
    temp=x
    x=y
    y=temp
x="india"
y="south africa"
swap(x,y)
print(y)

#example
def myfunction(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
myfunction(first="vishnu", second="sachin")

#cube
def cube(x):
    return x**3
cube(4)
for i in range(1,10):
    if i>100:
        break
    print(cube(i))
cube(7)

#arg
def my_f(arg1, *arg2):
    print("enter the first one :", arg1)
    for arg in arg2:
        print(arg)
my_f("vishnu", "vardhan", "reddy")

#fib
def fib(value):
    a,b=0,1
    while a<value:
        yield a
        a,b=b,a+b

#example
s="i love coding"
def f():
    print(s)
    
#example2
def func():
    s="Want to become a millionaire"
    print(s)
s="Also want to become a billionaire"
func()
print(s)

def add(a,b):
    c=a+b
    c=a*b
    c=a/b
    print(c)
add(4,5)

#class
class dog:
    attr1="animal"
    attr2="pet"
    def fun(self):
        print(self.attr1)
        print(self.attr2)
rodger=dog()
print(rodger.attr2)
rodger.fun()

#2
class dog:
    attr1="mammal"
    attr2="pet"
    def fun(self):
        print("i am a ", self.attr1)
        print("i am a", self.attr2)
pug=dog()
print(pug.attr1)
pug.fun()

#3
class dog(attr1="mammal", attr2="pet"):
    def fun(self):
        print("it's a ", self.attr1)
        print("it's a ", self.attr2)
pug=dog()
print(pug.attr2)
pug.fun()

#2nd example
class person:
    def __init__(self, name):
        self.name=name
    def my_name(self):
        print("my name is", self.name)
p=person("vishnu")
print(p.my_name())

class Dog:
    animal="dog"
    def __init__(self,breed,colour):
        self.breed=breed
        self.colour=colour
rodger=Dog("pug", "white")
buzo=Dog("german shepherd", "black")
print("rodger details")
print("it is a", rodger.breed)
print("it is a ", rodger.colour)

#addition
class addition:
    first=0
    second=0
    answer=0
    def __init__(self,f,s):
        self.first=f
        self.second=s
    def getinfo(self):
        print("first number is", str(self.first))
        print("second number is", str(self.second))
        print("answer is", str(self.answer))
    def calculate(self):
        self.answer=self.first+self.second
number=addition(1000,2000)
number.calculate()
number.getinfo()


#inheritance
class person:
    def __init__(self,name):
        self.name=name
        
    def details(self):
        return self.name
    def employee(self):
        return False
class isemployee(person):
    def employee(self):
        return True
emp=person("vishnu")
print(emp.employee(), emp.details)

nemp=isemployee("Vishnu vardhan")
print(nemp.employee())

#class inheritance

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print("my name is", self.name)
        print("my age is", self.age)
class person_details(person):
    def __init__(self,name,age,gender,colour):
        self.gender=gender
        self.colour=colour
        person.__init__(self,name,age)
a=person_details("vishnu",24,"male","white")
a.details()


#multilevel inheritance
self.str1,self.str2)
b=all_details()
b.my_details()
        class name:
    def __init__(self):
        self.str1="vishnu"
        print("Name")
class gender:
    def __init__(self):
        self.str2="male"
        print("Gender")
class all_details(name,gender):
    def __init__(self):
        name.__init__(self)
        gender.__init__(self)
        print("derived")
    def my_details(self):
        
#example
class child:
    def __init__(self,name):
        self.name=name
    def name(self):
    
        return self.name
    def isstudent(self):
        return False
def clas(child):
    def isstudent(self):
        return True
sn=child("sachin")    
print(sn.name(), sn.isstudent())    

#parent
class parent:
    fathername=""
    def father:

#add two number
num1=int(input("enter the first number: "))
num2=int(input("enter second number: "))
result=num1+num2
print("sum of {} and {} is {}".format(num1,num2,result))
#max
num1=int(input("enter the first number: "))
num2=int(input("enter second number: "))
if num1>num2:
    print("num1 is greater")
else:
    print("num2 is greater")
#maximum method2
def maximum(a,b):
    if a>b:
        return a
    else:
        return b
print(maximum(4,3))

num1=int(input("enter the first number: "))
for i in range(1,num1+1):
    while i>=num1:
        print (i*num1)
        i-=num1

def factorial(n):
    return 1 if(n==1 or n==0) else n*factorial(n-1)
factorial(10)
factorial(5)

#2nd method
def factor(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        while n>1:
            fact=fact*n
            n=n-1
        return fact
print(factor(6))
3/2
3//2
#simple interest
def simple_interest(p,t,r):
    si=(p*t*r)/100
    return si
print(simple_interest(1,2,3))

#prime numbers
for i in range(1,100):
    if i>1:
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            
            print(i)
#example
one="name"+"1"
print(one)
foo="bar"            
foo+=3
mouse+cat+dog="s"+"m"+"n"

#oops
class dog:
    attr1="mammal"
    attr2="doggie"
    def fun(self):
        print("I am a", self.attr1)
        print("Iam a ", self.attr2)
rodger=dog()
print(rodger.attr1)
rodger.fun()

#init method
class person:
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        print("Hello ", self.name)
p=person('Vishnu')
p.say_hi()

#example
class details:
    relation="lovers"
    def __init__(self,name,colour,looks, relation,):
        self.name=name
        self.colour=colour
        self.looks=looks
        self.relation=relation
women=details("paddu", "pure white","sexy","husband")
print("Her name is", women.name)
print("Her colour is", women.colour)
print("She looks", women.looks)
print("vishnu is her",women.relation)
print("vishnu is nothing without", women.name)

class geek:
    def __init__(self):
        self.geek="geeksforgeeks"
    def nyfun(self):
        print(self.geek)
n=geek()
n.nyfun()

class addition:
    first=0
    second=0
    answer=0
    def __init__(self,f,s):
        self.first=f
        self.second=s
    def display(self):
        print("first number is", self.first)
        print("second number is", self.second)
    def calculate(self):
        self.answer= self.first+self.second
add=addition(12,13)
add.calculate()
add.display()

#inheritance
class base1(object):
    def __init__(self):
        self.str1="vishnu"
        print("king")
class base2(object):
    def __init__(self):
        self.str2="virat"
        print("agression")
class derive(base1,base2):
    def __init__(self):
        base1.__init__(self)
        base2.__init__(self)
        print("derive")
    def func(self):
        print(self.str1,self.str2)
ob=derive()
ob.func()

#polymorphism
class india():
    def capital(self):
        print("delhi is the capital of india")
    def type(self):
        print("India is developing country")
    def leader(self):
        print("Jagan mohan reddy is the best leader in india")
class america():
    def capital(self):
        print("washinton is the capital of america")
    def type(self):
        print("us is developed country")
    def leader(self):
        print("obama is the best leader in us")
def myfun(obj):
    obj.capital()
    obj.type()
    obj.leader()
country1=india()
country2=america()
myfun(country1)
myfun(country2)

#exception handling
a=[1,2,3]
try:
    print("first index number is", a[0])
    print("second index number is", a[1])
    print("fourth index number is", a[4])
except IndexError:
    print("index error occured")
    
#exceptions
def divison(x,y):
    try:
        
        result=x//y
        print("you can divide", result)
    except ZeroDivisionError:
        print("cant divide with zero")
divison(4,2)
divison(4,3)   
divison(1,0)                                      
locals()['__builtins__']

#newone
try:
    a=10//0
    print(a)
except ArithmeticError:
    print("an error occured")
else:
    print("success")
    
#inpit
n,k= raw_input()
n=int(n)
k=int(k)
print(n, " ",k)

#lists
scores=[1,2,3,4]
scores[0]
scores[-1:-2]
scores[:]
li=[['a','b']]
li[-1][-1]

#functions
def add_sub(x,y):
    add=x+y
    sub=x-y
    return add,sub
add_sub(5,4)
result=add_sub(2,3)
print(result)

#functions
def person(name,age):
    print(name)
    print(age-5)
person("vishnu", 26)

#2nd example
def person(name,age):
    return name,age
person("vishnu",26)