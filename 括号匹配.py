# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 12:59:46 2018

@author: Administrator
"""

s = "()))"
if s == "":
    k = 0


temp=[]
temp.append(s[0])
i = 0 

for j in range(1,len(s)):
    if s[j] == "}" or s[j] =="]" or s[j] ==")":
        if i == -1:
            k = 0
        elif s[j] == "}" and temp[i] == "{":
            del(temp[i])
            i = i -1
        elif s[j] == "]" and temp[i] == "[":
            del(temp[i])
            i = i -1
        elif s[j] == ")" and temp[i] == "(":
            del(temp[i])
            i = i -1
        else:
            k = 0
    else:
       
        i = i+1
        temp.append(s[j])
        

if  len(temp) == 0:
    k = 1
else:
    k = 0
         
        