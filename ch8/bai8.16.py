# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 17:17:05 2020

@author: huybv1998
"""
import math

def CheckPrime(n):
    if (n < 2):
        return False
    for i in range(2, math.floor(math.sqrt(n))+1):
        if (n % i == 0):
            return False
        
    return True

print(CheckPrime(10))