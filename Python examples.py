# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 09:56:20 2021

@author: user
"""
#add two numbers
a=20
b=5
c=a+b
print("The sum of {} and {} is {}".format(a,b,c))
#example2 if we do not give int then it will consider it as string and the output will be concatination of 2inputs
a1=int(input("enter the number"))
b1=int(input("enter the second number"))
c1=a1+b1
print("the sum of {} and {} is {}".format(a1,b1,c1))

#squareroot
num=8
sqrt=num**0.5
print(sqrt)

#for complex numbers
import cmath
number=1+2j

print(cmath.sqrt(number))

#area of a triangle
p=float(input("enter the first side "))
q=float(input("enter the second side "))
r=float(input("enter the third side "))
s=(p+q+r)/2
aot=(s*(s-p)*(s-q)*(s-r))**0.5
print("The area of a triangle for sides {}, {} and {} is {}".format(p,q,r,aot))

#swaping two variables
x=5
y=6
x,y=y,x
print(x)
print(y)

#example 2
temp=x
x=y
y=temp
print(x)
print(y)

#genrating a random number
import random
print(random.randint(0,9))

#number guessing game
import random
import math
upper=int(input("enter the upper number "))
lower=int(input("enter the lower number "))
x=random.randint(lower,upper)
print("you've only", round(math.log(upper-lower+1,2)), "chances to guess")
count=0
while count < math.log(upper-lower+1,2):
    count+=1
    guess=int(input("enter a number"))
    if x==guess:
        print("you've guessed it correct")
        break
    elif x>guess:
        print("you've guesses low")
    elif x<guess:
        print("you've guessed high")
if count >=math.log(upper-lower+1,2):
    print("the number is ", x)
    print("better luck next time")
    
kilometer=int(input("enter total kilometres "))
conv=0.621371
miles=kilometer*conv
print("{} is equal to {} miles".format(kilometer,miles))


# checking whether a number is postive negative or zero
num=int(input("Please enter the number : "))
if (num%2)==0:
    print("Even Number")
else:
    print("Odd Number")
    
#leapyear
Year=int(input("Please enter the year : "))
if Year%4==0:
    if Year%100==0:
        if Year%400==0:
            print("It is a Leap Year")
        else:
            print("It is not a Leap Year")
    else:
        print("it is leap year")
else:
    print("It is not a leap year")

#largest number
num1=int(input("Enter the first Number: "))
num2=int(input("Enter the second Number: "))
num3=int(input("Enter the third Number: "))
if (num1>=num2) and (num1>num3):
    print("First number is greater")
elif(num2>=num1) and (num2>=num3):
    print("second num is greater")
else:
    print("third num is greate")


#primenumber
prime_number=int(input("enter number : "))
if prime_number>1:
    for i in range(2,prime_number):
        if (prime_number%i)==0:
            print("it is not a prime number")
            print(i, "time", prime_number/i, "is",prime_number)
            break
    else:
        print("it is a prime number")

else:
    print("it is not a prime number")

for i in range(1,10):
    print(i)
    
#prime numbers
lower=int(input("enter the lower num"))
upper=int(input("enter the higher num"))
for num in range(lower, upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
            
#factorial
num=int(input("enter the number: "))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
    print(factorial)

#multiplication
num=int(input("multiplaction of 12:"))
for i in range(1,11):
    x=num*i
    print(num, "X",i, "=",x)

#fibonnaci series
nterms=int(input("please enter the nterm"))
n1,n2=0,1
count=0
if nterms<0:
    print("please enter positive term")
elif nterms==1:
    print(n1)
else:
    print("fibonnaci series")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
        
#natural numbers
num=int(input("please enter the natural number: "))

if num<0:
    print("please enter positive number")
else:
    sum=0
    while (num>0):
        sum+=num
        num-=1
        
    print("the sum is", sum)
#powers
terms=int(input("please enter the term:"))
result=list(map(lambda x:3**x, range(terms)))
for i in range(terms):
    print(result[i])

#divisible
my_list=[1,13,26,42,35]
division=list(filter(lambda x:(x%13==0), my_list))

print(division)


#2nd example     
my_div=[]
for i in range(1,100):
    my_div.append(i)
div=list(filter(lambda x:(x%13==0), my_div))
print(div)

#decimal systems
number=int(input("Please enter the number: "))
print("The decimal systems number are")
print(bin(number), "in binary")
print(oct(number), "in octal")


#ascii
a=121
print("The ascii value of", a, "is", ord(a))
print("the ascii value of", a, "is", chr(a))


#factors
factors=int(input("Please enter the number: "))
for i in range(1,factors+1):
    if factors%i==0:
        print(i)
#calculator
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("select the operation")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.divison")
while(True):
    choice=int(input("please enter your choice"))
    if choice in(1,2,3,4):
        num1=float(input("Please enter your number"))
        num2=float(input("please enter your 2nd number"))
        if choice==1:
            print(num1, "+", num2, "is", add(num1,num2))
        elif choice==2:
            print(num1, "-", num2, "is", sub(num1,num2))
        elif choice==3:
            print(num1, "*", num2, "is", mul(num1,num2))
        elif choice==4:
            print(num1, "/", num2, "is", div(num1,num2))
        break
    else:
        print("invalid")

#calendar
import calendar
year=int(input("please enter year: "))
month=int(input("please enter month: "))
print(calendar.month(year,month))   


#fibonaci
def fibonaci_series(x):
    if x<=1:
        return x
    else:
        return(fibonaci_series(x-1)+fibonaci_series(x-2))
nter=100
if nter<=0:
    print("please enter positive number")
else:
    for i in range(nter):
        print(fibonaci_series(i))

#sum of natural number
def natural_number(n):
    if n<=1:
        return n
    else:
        return n+natural_number(n-1)
number=int(input("plese enter number"))
if number <=0:
    print("please enter positive number")
else:
    print("The sum of", number, "is",natural_number(number))
    
#factorial
def factorial(n):
    if n<=1:
        return n
    else:
        return n*factorial(n-1)
no=int(input("please enterthe number: "))
if no<=0:
    print("please enter positive number")
else:

    print("the sum is", factorial(no))
    
#palindrome
name="madam"
name.casefold()
nam1=reversed(name)
if list(name)==list(nam1):
    print("it is palindrome")
else:
    print("it is not a palindrome")
    
#sort
sort= "Vishnu"
words=[word.lower() for word in sort.split()]
words.sort()
for word in words:
    print(word)
    
#timer
import time
def timer(time_sec):
    while time_sec:
        min,sec=divmod(time_sec, 60)
        timeformat='{:02d}:{:02d}'.format(min,sec)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec-=1
    print("stp")
timer(10)

#remove duplicates
list1=[1,2,3,4,5,6,1,2,3]
print(list(set(list1)))


#occurence of character in a string
count=0
name="vishnu vardhan reddy"
char='v'
for i in name:
    if i==char:
        count+=1
print(count)
print(name.count(char))

digits=25.6787
abs(digits)
