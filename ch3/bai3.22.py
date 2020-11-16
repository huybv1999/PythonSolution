# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:01:35 2020

@author: huybv1998
"""
n = int(input("nhap 1 so n : "))
nearest_prime = 0
if (n < 3):
    pass
for i in range(n+1,2*n):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        nearest_prime = i
        break
print(nearest_prime)
    