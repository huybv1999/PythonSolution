# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 21:30:21 2020

@author: huybv1998
"""
s = "asdfkasdflasDfl222@424huy*&%$%&*("

notdigits = sum(not c.isdigit() for c in s)
notletters = sum(not c.isalpha() for c in s)
print("Không là số: ", notdigits)
print("Không là chữ: ", notletters)