# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 21:34:08 2020

@author: huy
"""

A = [1.2, "one" , 0.15, "A", "B", "C", 1, 50, 4.56, "C"]
B = [s for s in A if isinstance(s, (int, float))]
print(B)