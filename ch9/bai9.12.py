# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 22:40:19 2020

@author: huybv1998
"""
def fullstrip(s):
    s = " ".join(s.split())
    return s

s = "  Hà Nội thủ đô  của Việt   Nam   "
print(fullstrip(s))