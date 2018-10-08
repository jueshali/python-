# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:57:21 2018

@author: Administrator
"""

target = 8

candidates = [2,3,5]

mytarget = 0
temp = []
ans = []

def back(candidates,mytarget,temp):
    if mytarget >= target:
        if mytarget == target:
            temp.sort()
            if temp not in ans:
                ans.append(temp)
        return
    for i in candidates:
        temps = temp[:]
        temp.append(i)
        back(candidates,mytarget+i,temp)
        temp = temps[:]
back(candidates,mytarget,temp)