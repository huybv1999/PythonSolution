# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:15:36 2020

@author: huybv1998
"""
n = int(input("nhap 1 so n : "))
for i in range(1, n):
    sum1 = 0
    for j in range (1, i):
        if (i % j == 0):
            sum1 += j
    if (sum1 == i):
        print(sum1)
        