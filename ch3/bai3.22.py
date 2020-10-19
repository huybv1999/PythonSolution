# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:01:35 2020

@author: huybv1998
"""
n = int(input("nhap 1 so n : "))
if (n % 2 == 0):
    print(2)
i = 3
while (i*i <= n):
    if (n % i == 0):
        print(i)
    i += 1
    