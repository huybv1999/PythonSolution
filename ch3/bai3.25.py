# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:26:58 2020

@author: huybv1998
"""

n = int(input("Nhập số n: "))
for i in range(2, n):
   j = i + 2
   b1, b2 = False, False 
   i1 = 2
   while i1 < i and i % i1 != 0:
       i1 += 1
   b1 = i1 == i
   i2 = 2
   while i2 < j and j % i2 != 0:
       i2 += 1
   b2 = i2 == j
   
   if (b1 and b2):
       print("{:d} and {:d}".format(i, j))
   
           
