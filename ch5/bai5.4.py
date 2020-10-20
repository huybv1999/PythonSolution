# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:21:34 2020

@author: huy
"""
class Hocsinh:
    def __init__(self, Name, address, height, weight, gpa):
        self.name = Name
        self.address = address
        self.height = height
        self.weight = weight
        self.gpa = gpa
    
    def UpdateAdress(self, address):
        self.address = address
    
    def UpdateWH(self, height, weight):
        self.height = height
        self.weight = weightUpdateGPA
    
    def UpdateGPA(self, gpa):
        self.gpa = gpa
    
# =============================================================================
# Đây là phần ví dụ
# a = Hocsinh("Huy", "Vĩnh phúc", 173, 56, 8.5)
# a.UpdateAdress("Ba đình")
# a.UpdateWH(174, 60)
# a.UpdateGPA(9.0)
# =============================================================================
