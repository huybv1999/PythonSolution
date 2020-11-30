# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 22:31:32 2020

@author: huybv1998
"""

def TrongSau(s1, s2):             #9.21a
    return s1.find(s2) != -1

def findStringWithoutOverlapping(s1,s2):    #9.21b
    count = 0
    if (len(s2) > len(s1)):
        return 
    while (s1.find(s2) != -1):
        s1 = s1.replace(s2,"",1)
        count += 1
        continue
    return count
            
def findStringWithOverlapping(s1,s2):     #9,21c
    count = 0
    if (len(s2) > len(s1)):
        return 
    while (s1.find(s2) != -1):
        s1 = s1.replace(s2[0],"",1)
        count += 1
        continue
    return count
            
s1 = "abababababaab"
s2 = "aba"

print(TrongSau(s1,s2))
print("Xuất hiện: ", findStringWithoutOverlapping(s1,s2), "lần")
print("Có thể trồng lên: ", findStringWithOverlapping(s1,s2), "lần")