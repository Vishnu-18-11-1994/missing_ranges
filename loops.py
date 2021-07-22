# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 13:42:54 2021

@author: user
"""

name='vishnu'
for n in name:
    print(n)
    if n=='s':
        break

#2nd example
name='sachin'
for a in name:
    if a=='h':
        break
    print(a)

#example 3
names= ['Paddu', 'Padma','Padmavathi', 'Vishnu', 'vishnu vardhan']
for name in names:
    print(name)
    if name=='Padmavathi':
        print("She is vishnu's wife")
    elif name=='Padma':
        print("She is beautiful")
    elif name=='Paddu':
        print("She is sweet and cute")
    else:
        print("out of the loop")

#while loops
counter=1
sum=0
while (counter<=20):
    print(counter)
    
    sum=sum+counter
    counter=counter+1
print(sum)

#example2
number=1
add=0
while (number<=1):
    print(number)
  #  number=number+1
    add=add+number
    number=number+1
print(add)

#example 3
number1=0
number2=0
while (number1<=100):
    print(number1)
    number2+=number1
    number1+=1
print(number2)

#example3

height=4000
velocity=40
time=0
while(height>0):
    height-=velocity
    time+=1
print(height)
print(time)
name="vishnu"
a=[]
for w in name:
    a.append(w)
print(a)

for i in range(2.0):
    print(i)
    
#loops
name='Vishnu '
for i in range(1,8):
    print(name*i)
for i in range(7,0,-1):
    print(name*i)

name="vishnu"
for i in name:
    for pos in range(1,7):
        if i=='v':
            print(i*pos)
            continue
        if i=='i':
            print(i*pos)
            break
x = 2
for i in range(x):
      for j in range(x):
            a = x - j + i
            print(a)
#seaborn
import seaborn as sns
import matplotlib.pyplot as plt
data=sns.load_dataset('iris')
sns.lineplot(x='sepal_length', y='sepal_width', data=data)
plt.title("Seaborn using matplot")
plt.xlim(5)
sns.set_style('dark')
sns.despine()
plt.show()

#pyramid
name='koumudi'
for i in range(1, len(name)+1):
    print(name*i)
for j in range(len(name), 0, -1):
    print(name*j)
