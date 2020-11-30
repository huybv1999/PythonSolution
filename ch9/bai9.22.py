# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 22:49:40 2020

@author: huybv1998
"""
s = input("Nhập vào 1 sâu: ")
u = len(s)
for i in s: 
  s = i + s
print(s[:u])