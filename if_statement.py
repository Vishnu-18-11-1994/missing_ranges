# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 16:09:12 2021

@author: user
"""

# if statement
name="Vishnu"
age=25
Hobby="coding"
if name=="Vishnu" and Hobby=="Playing":
    Hobby= "Not coding"
print(Hobby)

#2nd example
name="Vishnu"
age=25
Hobby="coding"

if name=="Vishnu" and Hobby=="coding":
    Hobby="programming"
print(Hobby)

#3rd example
name="Vishnu"
age=25
Hobby="coding"
if name=="sachin" and Hobby=="coding":
    name="bolt"
else:
    name="vishnu"
print(name)

#4th example
name="Vishnu"
age=25
Hobby="coding"
if name=="Vishnu" and age==25 or Hobby=="Not coding" :
    details=True
else:
    details=False

print(details)

#5th example
age=25
number=10
if age==25 and number==int("10"):
    age=True
print(age)

