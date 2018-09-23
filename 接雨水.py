# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 13:27:32 2018

@author: Administrator
"""

height = [0,1,0,2,1,0,1,3,2,1,2,1]

max_index = height.index(max(height))

l,r = 0,len(height) - 1

water_count = 0

temp = l

while l < max_index:
    temp = temp + 1
    if height[l] <= height[temp]:
        l = temp
    else:
        water_count = water_count + height[l] - height[temp]
        
temp = r    
while r > max_index:
    temp = temp - 1
    if height[r] <= height[temp]:
        r = temp
    else:
        water_count = water_count + height[r] - height[temp]