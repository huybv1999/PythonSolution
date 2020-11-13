# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 00:56:54 2020

@author: huybv1998
"""

A = []
B = []
n = int(input("Nhập số tự nhiên n: "))

for i in range(0, n):
    x = int(input("Nhập số thứ %d: " %(i+1)))
    A.append(x)

max_val = max(A)

find_prime = [True for i in range(max_val + 1)]
find_prime[0] = False
find_prime[1] = False

l = 2
while(l*l < max_val):
    if (find_prime[l]):
        for j in range(l*l, max_val+1,l):
            find_prime[j] = False
    l += 1

lenn = len(A)

for k in range(lenn):
    if find_prime[A[k]]:
        B.append(A[k])
        
print(B)
        
        
    