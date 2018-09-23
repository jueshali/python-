# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 15:45:46 2018

@author: Administrator
"""
nums = [1,1,3,5,-2]
list1 = []
dic1 = {}
for index1,target in enumerate(nums):
    if not dic1.has_key(nums[index1]):
        dic1[target] = index1
        target = -target
        dic = {}
        list2 = []
        for index,value in enumerate(nums):
            if dic.has_key(target - nums[index]):
                list1.append([-target,dic[target - nums[index]],index])
            else:
                dic[value] = index