# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 12:02:21 2020

@author: huybv1998
"""
""" Tim prime number tu 1 cho den n"""

n = int(input("nhap 1 so n : "))
# i = 2
# factors = []
# while i*i <= n:
#     if (n % i):
#         i += 1
#     else:
#         n /= i
#         factors.append(i)
# if (n > 1):
#     factors.append(int(n))
# factors = list(dict.fromkeys(factors))
# print(factors)
for i in range(1, int(n**0.5)+1):
    if ((n % i == 0)):
        for j in range(2,i):
            if (i % j == 0):
                break
        else:
            if (i > 1):
                print(i)