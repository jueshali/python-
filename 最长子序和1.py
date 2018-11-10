# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 15:58:16 2018

@author: Administrator
"""

def maxnum(num,i,j):
    if i == j:
        return num[i] if num[i]>0 else 0
    else:
        s1 = maxnum(num,i,(i+j)/2)
        s2 = maxnum(num,(i+j)/2+1,j)
        left = 0
        temp = 0
        for i in range(i,(i+j)/2+1)[::-1]:
            temp = num[i] + temp
            left = max(temp,left)
        right = 0
        temp = 0
        for i in range((i+j)/2+1,j+1):
            temp = num[i] + temp
            right = max(temp,right)       
        return max(left+right,s1,s2)
    
