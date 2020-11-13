# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 22:57:55 2020

@author: huybv1998
"""

from modules import MyTriangle

x = (input("Nhập 3 số a, b ,c : ").split())
a = int(x[0])
b = int(x[1])
c = int(x[2])
print(MyTriangle.isTriangle(a,b,c))
print(MyTriangle.Perimeter)