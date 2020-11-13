# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 01:19:19 2020

@author: huybv1998
"""
import math
def is_square(N):
    return N == math.isqrt(N) ** 2  #Bản python 3.8 đổ lên mới có isqrt

N = int(input("Nhập số tự nhiên N: "))
print(is_square(N))
    