# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 22:25:31 2020

@author: huybv1998
"""
string = input("Nhập 1 ký tự: ")
s = set(string)
a = ""
for i in string:
    if (i in a):
        pass
    else:
        a = a + i
print(a)