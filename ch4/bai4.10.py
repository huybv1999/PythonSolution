# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 22:03:57 2020

@author: huybv1998
"""
def convert():
    gio = int(input("nhập số giờ: ")) * 3600
    phut = int(input("nhập số phút: ")) * 60
    giay = int(input("nhập số giây: "))

    time = (gio + phut + giay)/86400
    return time

print(convert())

