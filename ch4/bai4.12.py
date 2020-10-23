# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 20:16:52 2020

@author: huy
"""
def ConvertCK():
    Tc = int(input("Nhập giá trị tính theo độ C: "))
    Tk = 273.15 + Tc
    print('%0.2f độ C = %0.2f độ K.' % (Tc, Tk))
    
ConvertCK()


