# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 19:18:48 2020

@author: huy
"""
import math
def Summary(n):
    sum = 0
    for i in range(0,n+1):
        sum += i
        
    return sum

def HaiSoNguyenTo(m,n):
    if (m >0 and n > 0):
        while (m != n):
            if (m > n):
                m = m - n
            else:
                n = n - m
            
        if (m == 1):
            print("Hai số này là hai số nguyên tố cùng nhau" + "\n")
        else:
            print("Hai số này không là hai số nguyên tố cùng nhau" + "\n")
            
def SecToHours(s):
    hours = math.floor(s/3600)
    s %= 3600
    minutes = math.floor(s / 60)
    s %= 60
    print(repr(hours) + ":" + repr(minutes) + ":" + repr(s))
    
def defineAbs(a, b):
    if (a-b < 0):
        return (a-b)*-1
    else:
        return (a-b)

print("Câu a: " + repr(Summary(100)) + "\n")
print("Câu b: \n")
HaiSoNguyenTo(3, 7) 
print("Câu c: ")
SecToHours(10400)
print("Câu d: ")
print(defineAbs(5, 7))
