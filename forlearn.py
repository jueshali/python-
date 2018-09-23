# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 14:19:37 2018

@author: Administrator
"""

"""
a = [1,3,5,5,6]
b = []
c = []

for index in range(len(a)):
    b.append(9-a[index])
    c.append(9-a[index])



list.sort(a)
list.sort(b)

"""

nums = [2,7,11,15]
target = 9
rlist = [1,1]
for index in range(len(nums)):
    if nums.count(target-nums[index]) != 0:
        idx = nums.index(target-nums[index])
        break
                
rlist[0] = idx
rlist[1] = index
