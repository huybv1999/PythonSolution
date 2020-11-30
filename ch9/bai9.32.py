# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 03:55:50 2020

@author: huybv1998
"""
Hoten = " Vũ Thị Thuý Hồng"
res = Hoten.strip().split(" ")
Dem = " ".join(res[1:len(res)-1])
print("họ - :", res[0])
if (not Dem):
    print("đệm không có ")
else:
    print("đệm -: ",Dem)
print("tên -: ", res[len(res)-1])