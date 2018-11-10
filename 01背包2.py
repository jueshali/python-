# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 16:56:32 2018

@author: Administrator
"""
l = [1,2,3,4,5,6,7]
k = sum(l)/2
n = len(l)
m = [[0] * k for i in range(n)]

jmax = min(l[0]-1,k)

for j in range(jmax):
    m[0][j] = 0
    
for j in range(jmax,k):
    m[0][j] = l[0]
    
for i in range(1,n):
    jmax = min(l[i]-1,k)
    for j in range(jmax):
        m[i][j] = m [i-1][j]
    for j in range(jmax,k):
        if m[i-1][j] + l[i] <= k:
            m[i][j] = m[i-1][j] + l[i]
        else:
            m[i][j] = m [i-1][j]
