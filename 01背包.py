# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 16:11:08 2018

@author: Administrator
"""

n = 5
c = 10
w = [2,2,6,5,4]
v = [6,3,5,4,6]


m = [[0] * c for i in range(n)]

jmax = min(w[n-1] -1 ,c)

for j in range(0,jmax):
    m[n-1][j] = 0
for j in range(jmax,c):
    m[n-1][j] = v[n-1]
    
for i in range(3,-1,-1):
    jmax = min(w[i] -1 ,c)
    for j in range(0,jmax):
        m[i][j] = m[i+1][j]
    for j in range(jmax+1,c):
        m[i][j] = max(m[i+1][j],m[i+1][j-w[i]]+v[i])