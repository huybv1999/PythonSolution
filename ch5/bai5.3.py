# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:54:55 2020

@author: huy
"""
class QuadrilSquare:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def DienTich(self):
        return self.w * self.h
    def ChuVi(self):
        return (self.w + self.h)*2
    
class Square(QuadrilSquare):
    def __init__(self, slides):
        self.w = slides
        self.h = slides
    
    
# =============================================================================
# Đây là phần ví dụ
# regtangle = QuadrilSquare(16, 5)
# square = Square(3)
# 
# print(regtangle.DienTich()) 
# print(regtangle.ChuVi())
# print(square.DienTich())       
# print(square.ChuVi())
# =============================================================================
