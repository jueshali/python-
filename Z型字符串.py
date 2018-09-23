# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 21:44:16 2018

@author: Administrator
"""

s = "A"
numRows = 3
k = 
if len(s) < numRows:
    A = 0
    exit()
k = (numRows-1)*2
b = list(s)
list_str = [""]*len)

for i in range(numRows):
    s = (numRows-i-1)*2
    temp = [s,k-s]
    index = 0
    index_count = i
    list_str.append(b[index_count])
    while (temp[index] + index_count)<(len(b)):
        if temp[index] == 0:
            if index == 0:
                index = 1
            else:
                index = 0
        else:
            list_str.append(b[temp[index] + index_count])
            index_count = temp[index] + index_count
            if index == 0:
                index = 1
            else:
                index = 0
    
    