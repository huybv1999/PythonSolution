# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 19:11:22 2020

@author: huy
"""

def nhuan(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
    
print(nhuan(2012))