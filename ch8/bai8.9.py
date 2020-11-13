# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 02:27:58 2020

@author: huybv1998
"""
from modules import MyMatrix

A =  [[4, 5,6], [5, 8, 9 ], [9, 10, 11]]

MyMatrix.ChangeColumn(A,0,2)

if (MyMatrix.isMatrix(A) == True):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print('%4d'%A[i][j], end="")
        print()
        