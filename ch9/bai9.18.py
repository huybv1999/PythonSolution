# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 18:30:26 2020

@author: huybv1998
"""
def Component(S,k):
    A = []
    A = S.split()
    if (k > len(A)):
        return ""
    return A[k-1]

print(Component("Hà Nội là Thủ đô của Việt Nam",2))