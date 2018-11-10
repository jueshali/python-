# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 09:27:25 2018

@author: Administrator
0 非常值得考虑
"""
s = "1"
a = len(s)
p = [1]*a
b = (x for x in range(a))
for i in b:
    if s[i] == "0":
        if s[i-1] < "3" and s[i-1] != "0":
            p[i] = p[i-2]
            p[i-1] = p[i-2]
            if i < a-1:
                p[i+1] = p[i-2]
                next(b)

    elif s[i-1] < "2" or s[i-1] == "2" and s[i] < "7":
        if i==1:
            p[i] = p[i-1]+1
        else:
            p[i] = p[i-1] + p[i-2] 
    else:
        p[i] = p[i-1]
