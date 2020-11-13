# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 00:03:18 2020

@author: huybv1998
"""
A = []
n = int(input("Nhập 1 số tự nhiên N: "))
for i in range(1, n):
    if (n % i == 0):
        A.append(i)
        
print(A)