# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:26:58 2020

@author: huybv1998
"""
n = int(input("Nhap 1 so n: "))
for i in range(2, n):
    j = i + 2
    if (n % i != 0 and n % j == 0):
        print("({:d},{:d})".format(i, j))
        