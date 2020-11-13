# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:50:41 2020

@author: huybv1998
"""
def generate_Primes(n):
    is_prime = [True for i in range(n + 1)]
    is_prime[0] = False
    is_prime[1] = False
    l = 2
    while(l*l < n):
        for i in range(l*l, n+1,l):
            is_prime[i] = False
        l += 1

    return [i for i, element in enumerate(is_prime) if (element == True)]

print(generate_Primes(1000))
            


            