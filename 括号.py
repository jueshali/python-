# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 11:00:18 2018

@author: Administrator
"""

s = ""
list1 = []
n = 3
left = 0
right = 0

def back(s,left,right):
    if len(s) == n*2:
        list1.append(s)
        return
    else:
        back(s+"(",left+1,right)
        back(s+")",left,right+1)
"""
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)
"""

back(s,left,right)