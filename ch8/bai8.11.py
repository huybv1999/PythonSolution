# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 23:41:05 2020

@author: huybv1998
"""
import math 
A = []
A.append(1)
for i in range(2, 1001):
    A.append(math.pow((1+1/i), i))

N = int(input('Nhập số n: '))
print(math.exp(1) - math.pow((1+1/N), N))        