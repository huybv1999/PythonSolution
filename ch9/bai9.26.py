# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 00:14:00 2020

@author: huybv1998
"""
s = '101'

res = 0
for i in range(len(s)):
    res = res * 2
    res = res + int(s[i])

print("Kết quả: " ,res)