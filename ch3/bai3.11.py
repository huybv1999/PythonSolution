# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""  @huybv1998"""

T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12 = 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
Nhuan1 = 0
Nhuan2 = 0
NamNhuan1, NamNhuan2 = False, False

while True:
    days1 = int(input("Nhập ngày thứ 1: ")) 
    months1 = int(input("Nhập tháng thứ 1: "))
    years1 = int(input("Nhập năm thứ 1: "))
    if (years1 % 4 == 0 and years1 % 100 != 0) or years1 % 400 == 0:
        NamNhuan1 = True
    if (months1 > 12 or days1 > 31 or (months1 == 4 and days1>30) or (months1 == 6 and days1>30) or
        (months1 == 9 and days1>30) or (months1 == 11 and days1>30) or (not NamNhuan1 and months1 == 2 and days1>28)
        or (NamNhuan1 and months1 == 2 and days1>29)):
        print("Bạn đã nhập sai, xin hãy thử lại")
        continue
    days2 = int(input("Nhập ngày thứ 2: ")) 
    months2 = int(input("Nhập tháng thứ 2: "))
    years2 = int(input("Nhập năm thứ 2: "))
    if (years2 % 4 == 0 and years2 % 100 != 0) or years2 % 400 == 0:
        NamNhuan2 = True
    if (months2 > 12 or days2 > 31 or (months2 == 4 and days2>30) or (months2 == 6 and days2>30) or
        (months2 == 9 and days2>30) or (months2 == 11 and days2>30) or (not NamNhuan2 and months2 == 2 and days2>28)
        or (NamNhuan2 and months2 == 2 and days2>29)):
        print("Bạn đã nhập sai, xin hãy thử lại")
        continue
    break


if (months1 <= 2):
    years1 -= 1
Nhuan1 = int(years1 / 4 - years1 /100 + years1/400)

if (months2 <= 2):
    years2 -= 1
Nhuan2 = int(years2 / 4 - years2 /100 + years2/400)

n1 = years1 * 365 + days1
if (months1 == 1):
    pass
elif (months1 == 2):
    n1 += T1   
elif (months1 == 3):
    n1 += T1 + T2 
elif (months1 == 4):
    n1 +=  T1 + T2 + T3 
elif (months1 == 5):
    n1 += T1 + T2  + T3 + T4 
elif (months1 == 6): 
    n1 += T1 + T2 + T3 + T4 + T5 
elif (months1 == 7):
    n1 +=  T1 + T2 + T3 + T4 + T5 + T6  
elif (months1 == 8):
    n1 += T1 + T2 + T3 + T4 + T5 + T6 + T7
elif (months1 == 9):
    n1 +=  T1 + T2 + T3 + T4 + T5 + T6 + T7 + T8 
elif (months1 == 10):
    n1 += T1 + T2 + T3 + T4 + T5 + T6 + T7 + T8 + T9 
elif (months1 == 11): 
    n1 += T1 + T2 + T3 + T4 + T5 + T6 + T7 + T8 + T9 + T10 
elif (months1 == 12): 
    n1 += T1 + T2 + T3 + T4 + T5 + T6 + T7 + T8 + T9 + T10 + T11 
    

n1 += Nhuan1

n2 = years2 * 365 + days2
if (months2 == 1):
    pass
elif (months2 == 2):
    n2 += T1   
elif (months2 == 3):
    n2 += T1 + T2 
elif (months2 == 4):
    n2 +=  T1 + T2 + T3
elif (months2 == 5):
    n2 += T1 + T2  + T3 + T4
elif (months2 == 6): 
    n2 += T1 + T2 + T3 + T4 + T5 
elif (months2 == 7):
    n2 += T1 + T2 + T3 + T4 + T5 + T6  
elif (months2 == 8):
    n2 += T1 + T2 + T3 + T4 + T5 + T6 + T7
elif (months2 == 9):
    n2 +=  T1 + T2 + T3 + T4 + T5 + T6 + T7 + T8
elif (months2 == 10):
    n2 += T1 + T2 + T3 + T4 + T5 + T6 + T7 + T8 + T9 
elif (months2 == 11): 
    n2 += T1 + T2 + T3 + T4 + T5 + T6 + T7 + T8 + T9 + T10 
elif (months2 == 12): 
    n2 += T1 + T2 + T3 + T4 + T5 + T6 + T7 + T8 + T9 + T10 + T11 
    

n2 += Nhuan2

Delta = (n2 - n1)

print(Delta)
