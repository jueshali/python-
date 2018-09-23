# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:07:51 2018

@author: Administrator
"""

s = "+-1"
s = s.lstrip()

listtemp = ["1","2","3","4","5","6","7","8","9","0","+","-"]



b = s[0]

if b not in listtemp:
    k = 0

if b != "+" and b != "-":
    i = 0
else:
    i = 1

listnum = list(s)

while i < len(listnum):
    if listnum[i] not in listtemp:
        break
    i = i+1

num = int("".join(listnum[0:i]))