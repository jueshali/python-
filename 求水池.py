# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 12:32:48 2018

@author: Administrator
"""

b = [1,8,6,2,5,4,8,3,7]

right_index = 0
left_index = len(b) - 1
max_water = min(b[left_index],b[right_index]) * (left_index - right_index)

while right_index != left_index:
    if min(b[left_index],b[right_index])
    if b[right_index] > b[left_index]:
        max_water = max(b[left_index] * (left_index - right_index),max_water)
        left_index = left_index -1       
    else:
        max_water = max(b[right_index] * (left_index - right_index),max_water)
        right_index = right_index +1
        
       