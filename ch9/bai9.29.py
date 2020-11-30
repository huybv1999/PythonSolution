# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 02:28:51 2020

@author: huybv1998
"""
dec = 0
s = "ABCDEF"
check = False
hexdigits = "0123456789ABCDEF"
if (not s.isupper()):
    s = s.upper()
for char in s:
    if not (char in hexdigits):
        check = False
        print("Không phải là hệ hex")
        break
    else:
        check = True
if (check):
    for index, d in enumerate(s):
        sample = "0123456789ABCDEF"
        value = sample.index(d)
        p = (len(s) -(index+1))
        dec += (value*16**p)
print(dec)
    