# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 22:03:34 2018

@author: Administrator
"""
n = 5
p = [0 for i in range(n+1)]
p[0] = 1
p[1] = 1
for i in range(2,n+1):
    for k in range(1,i+1):
        p[i] = p[i]+p[i-k] * p[k-1]