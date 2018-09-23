# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 13:58:17 2018

@author: Administrator
"""

s = "MCMXCIV"

dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
temp = 1
count = 0
b = s[::-1]
for i in b:
    if dic[i] == temp:
        count = count + dic[i]
    elif dic[i] < temp:
        count = count - dic[i]
    else:
        temp = dic[i]
        count = count + dic[i]