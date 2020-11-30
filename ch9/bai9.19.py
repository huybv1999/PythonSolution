# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 19:52:05 2020

@author: huybv1998
"""
s = "asdfkasdflasDfl222@424huy*&%$%&*("

letters = sum(c.isalpha() for c in s)

print(letters)