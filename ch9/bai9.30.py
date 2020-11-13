# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 22:49:06 2020

@author: huybv1998
"""
s = input("Nhập 1 sâu: ")
A = ''.join([c for c in s if c.isdigit()])
s = ''.join([c for c in s if not c.isdigit()])
print(A + s[0:])