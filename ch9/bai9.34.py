# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 03:10:19 2020

@author: huybv1998
"""
HoTen = input("Nhập họ và tên: ")
res = HoTen.strip().split(" ")
word = input("Nhập từ cần đếm: ")
print(res.count(word))