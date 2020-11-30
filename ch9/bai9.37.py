# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 02:28:53 2020

@author: huybv1998
"""
def isSymmetry(s):
    check = True
    
    a = len(s)
    mid = int(a/2)
    if (a%2):
        mid += 1
    
    check1 = 0
    check2 = mid
    
    while(check1 < mid and check2 < a):
        if (s[check1] == s[check2]):
            check1 += 1
            check2 += 1
        else:
            check = False
            break
            
    return check

print(isSymmetry("baobao"))