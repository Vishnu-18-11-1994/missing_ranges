# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 10:28:14 2021

@author: user
"""

count=[1,2,3]
count.append(4)
count.extend([5,6])
count
count.append(8)
count
count.insert(6,7)
count
del count[7]
count
count.remove(5)
count
count.pop()
count
count.pop(4)
count
count.sort()
count
count.reverse()
count
count.clear()
count

#list comprehension
pow2=[2**x for x in range(20)]
pow2
sqrt=[x*x for x in range(10)]
sqrt

#example
list1=[1,2,3,(4,5)]
list1
list1[3]
#using keyword n
list_exist=[x*x for x in range(100) if x%2==1]
list_exist
print(2046 in list_exist)
print(5329 in list_exist)


#iterations
Powerful_persons=["Vishnu", "Jagan", "Modi"]
for x in Powerful_persons:
    print("The most powerful person in India is", x)
    
    
#tuples
my_tup=(1,2,3)
print(my_tup)
a,b,c=my_tup
print(a)
print(c)
print(my_tup+my_tup)
print(my_tup*3)


#strings
name="vishnu"
list(enumerate(name))
len(name)
print("Hi vishnu\nHow are you?")
print("Hi vishnu\vHow are you?")


#dictionaries
dict={"Name":"vishnu", "age":26}
dict['Name']
dict['age']
type(dict)
dict['age']=25
dict

marks={}.fromkeys(["english", "science","social"],0)
print(marks)
details={}.fromkeys(["name","age","gender"], "vishnu",26,"male")
print(details)