# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 22:59:21 2020

@author: huybv1998
"""
a = [0,2,4,6,8,10]
b = [1,3,5,7,9,11,13,15]  #Ví dụ
c = []

findmax = []

findmax.append(len(a))
findmax.append(len(b))

for i in range(max(findmax)):
    if (i >= min(findmax)):
        if (len(b) == 0 and len(a) != 0):
            c.append(a.pop())
            continue 
        else:
            c.append(b.pop())
            continue 
    else:
        c.append(a.pop())
        c.append(b.pop())    
 