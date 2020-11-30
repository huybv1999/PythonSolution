# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 22:49:51 2020

@author: huybv1998
"""
Str = "BùiVũHuy"
St = "Hoàng"
print(Str)
while True:
    k = int(input("Nhập vị trí bạn muốn chèn: "))
    if (k > len(Str)):
        print("Bạn k thể chèn vào vị trí đó")
        continue
    break
print(Str[:k] + St + Str[k:]) 