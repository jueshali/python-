# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 21:53:33 2018

@author: Administrator
"""
"""
时间超过限制
"""

nums = [0,2,2,3,0,1,2,3,-1,-4,2]
temp = [0,2,2,3,0,1,2,3,-1,-4,2]    
a = []
for target in nums:
     dic = {}
     temp.remove(target)
     for index,value in enumerate(temp):
         b = -target - temp[index]
         if dic.has_key(b):                 
             temp1 = [temp[dic[b]],temp[index],target]
             temp1.sort()
             if temp1 not in a:
                 a.append(temp1)
         else:
             dic[value] = index
"""

    b = a

b.remove(2)

a = [1,2,3]
"""