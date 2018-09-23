# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 18:58:40 2018

@author: Administrator
"""

strs = ["flower","flow","flight"]

temp = strs[0]

for i in range(1,len(strs)):
    while not temp in strs[i][0:len(temp)]:
        temp = temp[:-1]
 