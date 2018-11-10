# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 08:54:23 2018

@author: Administrator
"""

grid = [[1,3,1],[1,5,1],[4,2,1]]

m = len(grid)
n = len(grid[0])

for i in range(m):
    for j in range(n):
        if i==0 and j==0:
            pass
        elif i == 0:
            grid[i][j] = grid[i][j-1] + grid[i][j]
        elif j == 0:
            grid[i][j] = grid[i-1][j] + grid[i][j]
        else:
            grid[i][j] = min(grid[i][j-1],grid[i-1][j]) + grid[i][j]