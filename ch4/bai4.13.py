# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 20:21:58 2020

@author: huy
"""
def ConvertKC():
    Tk = float(input("Nhập giá trị tính theo độ K: "))
    Tc = Tk - 273.15
    print('%0.2f độ K = %0.2f độ C.' % (Tk, Tc))
    
ConvertKC()

def ConvertFK():
    Tf = float(input("Nhập giá trị tính theo độ F: "))
    Tk = 273.5 + ((Tf - 32.0) * (5.0/9.0)) 
    print('%0.2f độ F = %0.2f độ K.' % (Tf, Tk))

ConvertFK()

def ConvertKF():
    Tk = float(input("Nhập giá trị tính theo độ K: "))
    Tf = (Tk - 273.15)*9 /5 + 32
    print('%0.2f độ K = %0.2f độ F.' % (Tk, Tf))

ConvertKF()


def ConvertCF():
    Tc = float(input("Nhập giá trị tính theo độ C: "))
    Tf = 1.8 * Tc + 32
    print('%0.2f độ C = %0.2f độ F.' % (Tc, Tf))
    
ConvertCF()


def ConvertFC():
    Tf = float(input("Nhập giá trị tính theo độ F: "))
    Tc = (Tf - 32) * 5 / 9
    print('%0.2f độ F = %0.2f độ C.' % (Tf, Tc))
    
ConvertFC()