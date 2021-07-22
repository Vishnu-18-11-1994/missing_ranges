# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 16:37:21 2021

@author: user
"""

myUniqueList=[]
myLeftOvers=[]

def addToList(x):
    if(x in myUniqueList):
        myLeftOvers.append(x)
        return False
    myUniqueList.append(x)
    return True

assert True==addToList(1)
assert True==addToList(2)
assert False==addToList(2)
print(myUniqueList)
print(myLeftOvers)
3000/24

#plots
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[3,4,5,6,7]
plt.plot(x,y)
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.title("normal plot")
plt.axis([0,10, 1,20])

#2nd example
from matplotlib.figure import Figure
fig=plt.figure(figsize=(5,5))
ax=fig.add_axes([2,1,1,1])
ax.plot(x,y)

#3rd example
from matplotlib.figure import Figure
fig=plt.figure(figsize=(3,4))
ax=fig.add_axes([1,2,2,1])
ax1=ax.plot([2,3,4,5],[4,5,6,7])
ax2=ax.plot([2,3,4,5],[5,6,4,8])
plt.show()

#bar chart
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,3,4,5,6]
plt.bar(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Bar plot')
plt.legend(['Red'])

#example 4
year=[1910,1920,1930,1940,1950]
india=[100,200,300,400,500]
australia=[200,300,400,500,600]
plt.plot(year, india, label='Red')
plt.plot(year, australia, label='Yellow')
plt.xlabel('Team')
plt.ylabel('cricket')
plt.title('India and Australia')
plt.legend(['India', 'Australia'])

#subplot
x=[1,2,3,4]
fig,ax=plt.subplots(3,4)
ax[0].plot(x)

#example
import numpy as np
import matplotlib.pyplot as plt
import random
players=['sachin', 'sehwag', 'ganguly', 'dravid', 'laxman', 'kumble', 'dhoni', 'virat', 'rohit','zaheer']
rank=[]
for i in range(0, len(players)):
    rank.append(random.randint(0,101))
plt.xlabel("Players")
plt.ylabel('Rank')
plt.title("Players rank according to each individual")
plt.plot(players, rank, color='red', marker='s', markersize=15, markerfacecolor='blue', linestyle='solid')

#bar plot
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
barwidth=0.25
data={"Sachin":49, "Kohli":43, "ponting":30, 'rohit':29, 'sangakkara':25, "lara":19}
test_data={"Sachin":51, "kohli":27, "ponting":41, "rohit":6, "sangakkara":38, "lara":34}
batsmen=list(data.keys())
centuries=list(data.values())
test_batsmen=list(test_data.keys())
test_centuries=list(test_data.values())

figure=plt.subplots(figsize=(12,8))
plt.bar(batsmen, centuries, color='Red')
plt.bar(test_batsmen,test_centuries, color='Blue')
plt.xlabel("Players")
plt.ylabel("Centuries")
plt.title("Hundreds in Odi and test format")

#example
print("vishnu", end='.')

#example
import antigravity


#example
list=[1,0,3,0,4]
list.pop(1,3)
list.append(1,2)

#example