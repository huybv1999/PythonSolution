# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 23:20:55 2020

@author: huybv1998
"""
s1 = "Special $#! abc%^&*( characters   spaces 888323"
n1 = []
for i in range(48,58):
    n1.append(chr(i))
n = ''.join(c if c in map(str,n1) else "" for c in s1)