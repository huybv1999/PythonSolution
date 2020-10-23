# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:08:21 2020

@author: huy
"""
A = ['apple', 'banana', 'cherry', 'rero', 5, 6 , 7, '8']

def sumList(food):
    n = sum(filter(lambda x:isinstance(x,int),food))
    return n

def countString(food):
    count = 0
    for s in food:
        if isinstance(s, str):
            count += 1
    return count

def filterList(food):
    B = [i for i in food if isinstance(i, int)]
    C = [s for s in food if isinstance(s, str)]
    return B, C

print(countString(A))
print(sumList(A))
print(filterList(A))