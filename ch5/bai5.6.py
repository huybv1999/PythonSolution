# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 23:40:27 2020

@author: huy
""" 

class Triple:
    def __init__(self, a, b ,c):
        self.a = a
        self.b = b
        self.c = c
        self.S = a + b + c
        
        
    def Update(self):
        self.S = self.a + self.b + self.c
        return self.S

    
    def Change(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.S = self.a + self.b + self.c
        
    
    def isTriangle(self):
        if (self.a + self.b <= self.c) or (self.a + self.c <= self.b) or (self.b + self.c <= self.a) : 
            return False
        else: 
            return True

# =============================================================================
# Ví dụ
# triagle = Triple(5,6,7)
# triagle.Update()
# triagle.Change(7,5,10)
# triagle.isTriangle()
# 
# =============================================================================


class Tam_Giac(Triple):
    def getArea(self):
        s = self.S / 2
        area = (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        return area
    
    def getCircumcircle(self):
        s1 = self.a * self.b * self.c
        r = s1/((self.a + self.b + self.c)*(self.b + self.c - self.a)*(self.c + self.a - self.b)*(self.a + self.b - self.c))**0.5
        return r
    
    def getInscribeCircle(self):
        d = self.getArea()
        r = d/(self.S/2) 
        return r
    
# =============================================================================
# triagle = Triple(5,6,7)    
# triagle.Update()
# tam_giac = Tam_Giac(5, 6, 7)
# print(tam_giac.getArea())
# print(tam_giac.getCircumcircle())
# print(tam_giac.getInscribeCircle())
# =============================================================================
