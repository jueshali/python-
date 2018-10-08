# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 16:50:51 2018

@author: Administrator
"""

candidates = [10,1,2,7,6,1,5]
target = 8
ans = []
temp = []
count = 0
left = 0
right = len(candidates)-1
candidates.sort()

def back(count,candidates,temp):
    if count == target:
        ans.append(temp)
    if count > target:    
        return
    if count < target:


back(count,candidates,temp)