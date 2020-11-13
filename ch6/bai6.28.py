# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 02:05:27 2020

@author: huybv1998
"""
A = [30,70,4,6,8,10]
B = [6,12,5,7,9,11]
C = []
def gcd(x,y):
    while (y != 0):
        x = x + y
        y = x - y
        x = x - y
        if (y == 0):
            return x
        y = x%y
    return x

for i in range(len(A)):
    C.append(gcd(A[i],B[i]))
    