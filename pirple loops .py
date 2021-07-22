# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 16:32:28 2021

@author: user
"""

for number in range(1, 101):
    if (number%3)==0 and (number%5)==0:       
        print('FizzBuzz')
        continue
    if number%3==0:
        print('Fizz')
        continue
    if number %5==0:
        print('Buzz')
        continue                
    else:
        print(number)

#prime numbers
n=2
for i in range(1,101):
    while i>n:
        print("prime")

        n+=1
import time   
time.time()
