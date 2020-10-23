# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 19:05:20 2020

@author: huy
"""

def sign(x):
    if x > 0:
        return 1
    if x==0:
        return 0
    else:
        return -1

print(sign(6))