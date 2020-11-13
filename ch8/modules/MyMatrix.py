# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:00:36 2020

@author: huybv1998
"""

# A = [[4, 5,6], [5, 8, 9 ], [9, 10, 11]]

def isMatrix(A):
    res = all(isinstance(E, list) for E in A)
    if (len(A) == 0 or res == False):
        return False
    for i in range(1, len(A)):
        if (len(A[i]) != len(A[0])):
            return False
    return True
                    

def ChangeRow(A, i , j):
    if (isMatrix(A)):
        A[i], A[j] = A[j], A[i]
        return True
    return False

def ChangeColumn(A, i ,j):
    if (isMatrix(A)):
        for col in A:
            col[i], col[j] = col[j], col[i]
        return True
    return False

def isSquare(A):
    for row in A:
        if len(row) == len(A):
            return True
    return False

def GetSymmetry(A):
    tr = [[0 for j in range(len(A[0])) ] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):
            tr[i][j] = A[j][i]
    return tr


def GetInverse(A):
    n = len(A)
    I = [[0 for x in range(n)] for y in range(n)]
    for i in range(0, n):
        I[i][i] = 1
    for fd in range(n):
        fdScalar = 1 / A[fd][fd]
        for j in range(n):
            A[fd][j] *= fdScalar
            I[fd][j] *= fdScalar
        for i in list(range(n))[:fd] + list(range(n))[fd+1:]:
            crScalar = A[i][fd]
            for j in range(n):
                A[i][j] = A[i][j] - crScalar * A[fd][j]
                I[i][j] = I[i][j] - crScalar * I[fd][j]
    return I
                
# print(isMatrix(A))
# print()
# # ChangeColumn(A,0,2)
# if (isMatrix(A) == True):
#     for i in range(len(A)):
#         for j in range(len(A[0])):
#             print('%4d'%A[i][j], end="")
#         print()
        
# print(GetSymmetry(A))
