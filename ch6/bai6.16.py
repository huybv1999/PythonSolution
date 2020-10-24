# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 23:22:39 2020

@author: huy
"""

A = []
B = []
n = int(input("Nhập 1 số n: "))
for i in range(0, n):
    if (i % 2 == 0):
        A.append(i)
    if (i%2):
        B.append(i)
print(A)
   