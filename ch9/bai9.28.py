# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 21:48:53 2020

@author: huybv1998
"""
n = 156
c = []
while (n > 0):
    a = int(n%2)
    c.append(a)
    n = (n-a)/2
c.append(0)
res = ""
for i in c[::-1]:
    res = res + str(i)
print(res)
    
    