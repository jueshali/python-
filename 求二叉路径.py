# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 12:52:53 2018

@author: Administrator
"""
triangle = [[-1],[3,2],[-3,1,-1]]

floor = 0

for i in triangle:
    floor = floor + 1
    if i == triangle[0]:
        continue
    if i == triangle[1]:
        i[0] = i[0] + triangle[floor-2][0]
        i[1] = i[1] + triangle[floor-2][0]
        continue

    length = len(i)
    
    for j in range(length):
        if j == 0:
            i[j] = triangle[floor-2][j] + i[j]

        else:
            i[j] = min(triangle[floor-2][j],triangle[floor-2][j-1]) + i[j]