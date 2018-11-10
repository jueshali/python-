# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:48:32 2018

@author: Administrator
"""


obstacleGrid = [[0,0],[1,0],[0,0]]
m = len(obstacleGrid)
n = len(obstacleGrid[0])

path = [[0]*n for i in range(m)]

path[0][0] = 1

for i in range(m):
    for j in range(n):
        if i==0 and j==0:
            if obstacleGrid[0][0] == 1:
                path[0][0] = 0
            else:
                path[0][0] = 1
        elif i ==0 :
            if obstacleGrid[i][j-1] == 1:
                path[i][j] = 0
            else:
                path[i][j] = path[i][j-1]
        elif j ==0 :
            if obstacleGrid[i-1][j] == 1:
                path[i][j] = 0
            else:
                path[i][j] = path[i-1][j]
        else:
            if obstacleGrid[i-1][j] == 1 and obstacleGrid[i][j-1] == 1:
                path[i][j] = 0
            elif obstacleGrid[i-1][j] == 1:
                path[i][j] = path[i][j-1]
            elif obstacleGrid[i][j-1] == 1:
                path[i][j] = path[i-1][j]
            else:
                path[i][j] = path[i-1][j]+path[i][j-1]
d=path[m-1][n-1]