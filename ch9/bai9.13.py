# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 21:48:21 2020

@author: huybv1998
"""
def Tachten(Hoten):
    res = Hoten.strip().split(" ")
    final = res[len(res)-1]
    return final

s = " Nguyễn Quang   Bình   "
print(Tachten(s))