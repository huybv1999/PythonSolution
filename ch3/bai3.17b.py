# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 17:03:01 2020

@author: huybv1998
"""
x = int(input("nhap so n"))
y = 0
if (x < 0):
    print("nhap lai n")
for i in range(1,x):
    if (x % i == 0):
        y += i
print(y)
        
