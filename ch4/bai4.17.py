ín# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 23:47:37 2020

@author: huy
"""
def f(m,n):
    if (m == 0 or n == 0):
        return m+n
    while (m != n):
        if (m > n):
            m -= n
        else:
            n -= m
    
    if (m == 1 or n == 1):
        return 0
    else:
        return m
    
                
print(f(70,100))