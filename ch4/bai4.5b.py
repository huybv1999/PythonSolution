# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 22:58:01 2020

@author: huybv1998
"""
def f(m, n):
    count = 0
    for i in range(1, min(m,n)+1):
        if (m % i == 0 and n % i !=0 ):
            count += 1
    return count

print(f(36,45))