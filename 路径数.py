# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:20:44 2018

@author: Administrator
"""
m = 1
n = 1

path = [[0]*n for i in range(m)]

path[0][0] = 1

for i in range(m):
    for j in range(n):
        if i==0 and j==0:
            path[0][0] = 1
        elif i ==0 :
            path[i][j] = path[i][j-1]
        elif j ==0 :
            path[i][j] = path[i-1][j]
        else:
            path[i][j] = path[i-1][j]+path[i][j-1]