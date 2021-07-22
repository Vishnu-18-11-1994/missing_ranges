# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 12:57:14 2021

@author: user
"""
#method 1

def find_missing(list):
    return [x for x in range(list[0],list[-1]+1) if x not in list]
list=[1, 5, 9, 15, 25,40,70,100]
print(find_missing(list))




#method 2
def find_missing(list):
    lower=list[0]
    upper=list[-1]
    return sorted(set(range(lower, upper+1)).difference(list))
lower=1
upper=100
list=[1,5,10,15,25,40,50,65,80,100]
print(find_missing(list))