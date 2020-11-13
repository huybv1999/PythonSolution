# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:56:42 2020

@author: huybv1998
"""
#Câu 12.a
def SquareSum(n):
    if (n == 1):
        return 1
    if (n == 0):
        return 0
    return n**2+SquareSum(n-1)

#Câu12b
def SumPhanSo(n):
    sum1 = 0
    for i in range(1, n+1):
        sum1 += 1/(i)
    return sum1

#Câu 12.c
def SumPhanSo2(n):
    sum2 = 0
    for i in range(2, n+1):
        sum2 += 1/((i-1)*i)
        
    return sum2
    
    
n = int(input("Nhập 1 số n: "))
print(SquareSum(n))
print(SumPhanSo(n))
print(SumPhanSo2(n))
