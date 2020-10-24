# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 00:50:12 2020

@author: huy
"""
A = [1.2, "one" , 0, 15, "A", "B", "C", '54', 1, 50, 4.56, "C"]

def general_sort(A):
    B = []
    just_number = [i for i in A if isinstance(i, (int, float))]
    mark = [isinstance(s, str) for s in A]
    for i in range (0, len(just_number)-1):
        for j in range(0, len(just_number)-i-1):
            if (just_number[j] < just_number[j+1]):
                just_number[j], just_number[j+1] = just_number[j+1], just_number[j]  #Sort theo thứ tự ngược lại
                
    for pos in range(len(A)):
        if mark[pos]:
            B.append(A[pos])
        else:
            B.append(just_number.pop())
    return B

print(A)
print(SortKeepString(A))