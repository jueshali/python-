# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 17:02:49 2018

@author: jueshali
"""

num = 3884
l = []

a = num/1000

l.append("M"*a)

num = num - a*1000

a = num /100


if a==4:
    l.append("CD")
elif a == 9:
    l.append("CM")
elif a >= 5:
    l.append("D")
    l.append("C"*(a-5))
else:
    l.append("C"*a)
    
num = num - a*100
    
a = num /10

if a==4:
    l.append("XL")
elif a == 9:
    l.append("XC")
elif a >= 5:
    l.append("L")
    l.append("X"*(a-5))
else:
    l.append("X"*a)

num = num - a*10

a = num 

if a==4:
    l.append("IV")
elif a == 9:
    l.append("VI")
elif a >= 5:
    l.append("V")
    l.append("I"*(a-5))
else:
    l.append("I"*a)
    
s = "".join(l)