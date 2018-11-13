# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 21:20:57 2018

@author: Administrator
"""

b = [5,3,5,6,2,3,5]


def getmaxrl(b):
    max1 = b[0]
    for i in range(len(b)-1):
        max1  = max(b[i],max1)
        
    return max1-min(b[0],b[len(b)-1])