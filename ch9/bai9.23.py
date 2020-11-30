# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:12:33 2020

@author: huybv1998
"""
s1 = "Special $#! abc%^&*( characters   spaces 888323"
s2 = "12//n,_@#$%3.14kjlw0xdadfackvj1.6e-19&*ghn334"
n1 = [s for s in s1 if not s.isalnum()]
n1 = ' '.join(n1).split()
n2 = [s for s in s2 if not s.isalnum()]
n2 = ' '.join(n2).split()
n3 = []
c = []

n3.append(len(n1))
n3.append(len(n2))

for i in range(0, max(n3)):
    if i >= min(n3):
        if len(n1) == min(n3):
            c.append(n2[i])
            continue
        if len(n2) == min(n3):
            c.append(n1[i])
            continue
    else:
            c.append(n1[i])
            c.append(n2[i])
            
print(''.join(c))