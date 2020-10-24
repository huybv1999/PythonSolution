# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 19:29:10 2020

@author: huy
"""
def sort(somelist):
    n = len(somelist)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if (somelist[j] > somelist[j+1]):
                somelist[j], somelist[j+1] = somelist[j+1], somelist[j]
    
A = [8.8, 7, 5.5,3 ,2 , 10.6, 11.8, 12, 1 , 0]
sort(A)
print(A)