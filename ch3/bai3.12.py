# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:41:58 2020

@author: huybv1998
"""
n = int(input("Nhập 1 số n: "))
for i in range(2, n):
   if n % i == 0:
       print("n không phải là số nguyên tố")
       break
   else:
       print("n là số nguyên tố")
       break