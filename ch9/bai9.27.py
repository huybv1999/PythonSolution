# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 00:16:38 2020

@author: huybv1998
"""
s = "check110111"
check = False
c = "01"
for char in s:
    if not (char in c):
        check = False
        print("Không phải là nhị phân")
        break
    else:
        check = True

if check:
    res = 0
    for i in range(len(s)):
        res = res * 2
        res = res + int(s[i])

    print("Kết quả: " ,res)

    