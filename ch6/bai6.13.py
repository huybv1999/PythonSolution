# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 22:04:02 2020

@author: huybv1998
"""
A = [0,2,4,6,8,10]
B = [1,3,5,7,9,11]
c = []
a = []

a.append(len(A))
a.append(len(B))

for i in range(0, max(a)):
    if i >= min(a):
        if len(A) == min(a):
            c.append(B[i])
            continue
        if len(B) == min(a):
            c.append(A[i])
            continue
    else:
            c.append(A[i])
            c.append(B[i])
            
print(c)