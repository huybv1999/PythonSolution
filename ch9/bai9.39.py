# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 00:43:36 2020

@author: huybv1998
"""
s = '525253324244245555556666666666677'

a = len(s)

l = 1
lmax = 0
ld = [0] * a

for i in range(1, a):
    if (s[i] == s[i-1]):
        l += 1
        ld[i] = l
        if (l > lmax):
            lmax = l
            
    else:
        l = 1

#print(lmax)
for i in range(0,a):
    if (ld[i] == lmax):
        print(s[i+1-lmax:i+1])
        break
