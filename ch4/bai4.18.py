# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 23:29:22 2020

@author: huy
"""
import math
def factorial(n):
    if (n==1):
        return 1
    else:
        return n*factorial(n-1)

def sqrtfunction(n, i):
    if (n == i):
        return math.sqrt(i)
    else:
        return math.sqrt(n + (sqrtfunction(n+1, i)))
    
print(factorial(10))
