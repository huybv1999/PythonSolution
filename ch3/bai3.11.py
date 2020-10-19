# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""  @huybv1998"""

from datetime import datetime

date_format = "%d/%m/%Y"
a1 = input("Ngay thu 1: ")
a2 = input("Ngay thu 2: ")
a = datetime.strptime(a1, date_format)
b = datetime.strptime(a2, date_format)
delta = b - a
print(delta.days)