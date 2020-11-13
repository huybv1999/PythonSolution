# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 22:37:20 2020

@author: huybv1998
"""
import math

def isTriangle(a,b,c):
    if (a + b <= c) or (a+c <=b) or (b+c <= a):
        return False
    return True

def Perimeter(a,b,c):
    p = (a + b + c)
    return p

def Area(a,b,c):
    p2 = (a+b+c)/2
    S = math.sqrt(p2*(p2-a)*(p2-b)*(p2-c))
    return S