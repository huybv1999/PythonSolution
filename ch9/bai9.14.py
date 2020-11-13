# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 22:37:53 2020

@author: huybv1998
"""
s = "1 con vịt, 22 con sư tử, 32 con tê giác"
print(s)
numbers = sum(c.isdigit() for c in s)
print(numbers)