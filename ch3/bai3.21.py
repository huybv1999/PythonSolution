# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 12:02:21 2020

@author: huybv1998
"""
""" Tim prime number tu 1 cho den n"""

n = int(input("nhap 1 so n : "))
for num in range(0, n+1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
     