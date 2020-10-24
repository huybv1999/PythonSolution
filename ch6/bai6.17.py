# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:36:57 2020

@author: huy
"""
import random
A = []
B = []
C = []
n = int(input("Nhập n nhỏ hơn hoặc lớn hơn bằng 6: "))
for i in range(0, n):
    n = random.randint(5, 30)
    A.append(n)
    
for j in range(0, 6):
    n = random.randint(5, 30)
    B.append(n)
    
point = 0 # Bắt đầu cộng nếu độ dài b lớn hơn a hoặc ngược lại

print(A)
print(B)
if (len(B) > len(A)):
    C = B
    for i in A:
        C[point] = i + C[point] 
        point += 1
else:
    C= A
    for i in B:
        C[point] = i + C[point] 
        point += 1

print(C)
    

