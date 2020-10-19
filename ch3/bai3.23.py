# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:15:36 2020

@author: huybv1998
"""
n = int(input("nhap 1 so n : "))
sum1 = 0
for i in range(1, n):
    if (n % i == 0):
        sum1 += i
if (sum1 == n):
    print("so n la so hoan hao")
else:
    print("so n la so ko hoan hao")
    
        