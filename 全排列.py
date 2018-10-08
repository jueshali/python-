# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:04:26 2018

@author: Administrator
"""

s = "1bc"
ans = []
temp = ""
n = 0
t = list(s)
def back(temp,s,n):
    if len(temp) == 3:
       ans.append(temp)
       return
    if t[n].isdigit():
        back(temp+s[n].upper(),s,n+1)
    if t[n].isalpha():
        back(temp+s[n].upper(),s,n+1)
        back(temp+s[n].lower(),s,n+1)
       
       
back(temp,s,n)
           