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
        self.S = self.a + self.b + self.c
        
    def Update(self):
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

