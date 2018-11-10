# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 15:57:18 2018

@author: Administrator
"""

nums = [-2,-3,-1,-5]
maxval = 0
temp = 0
i = 0
while 1:
    if i == len(nums):
        break
    if temp < 0:
        temp = 0
        i = i - 1
    else:
        temp = temp + nums[i]
    maxval = max(temp,maxval)
    i = i + 1
if maxval == 0:
    maxval= max(nums)

"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return None
        maxval = 0
        temp = 0
        for i in nums:
            if temp > 0:
                temp = temp + i
            else:
                temp = i
            maxval = max(maxval,temp)
        if maxval > 0:
            return maxval
        else:
            return max(nums)
        """