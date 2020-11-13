# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 01:22:37 2020

@author: huybv1998
"""
import math

def calculateArea(a, b, c):
    p = (a + b + c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    ha = S/(0.5*a)     #Chỗ này đề bài bị sai 
    hb = S/(0.5*b)     #Không phải là 2*a mà là 0.5*a
    hc = S/(0.5*c)
    return ha, hb, hc

while True:
    x = (input("Nhập 3 số a, b ,c : ").split())
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])
    if ((a + b <= c) or (a + c <= b) or (b + c <= a)):
       print("Oops, xin hãy nhập lại")
       continue
    break
    
print(calculateArea(a, b, c))