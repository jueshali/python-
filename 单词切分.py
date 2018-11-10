# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 21:55:05 2018

@author: Administrator
"""

s = "leetcode"
wordDict=["leet","code"]

"""i = 0

for j in range(len(s)):
    if s[i:j+1] in wordDict:
        i = j + 1

c = 0 if i>j else 1
"""


"""
可以反着回来
"""
m = len(s)
p = [0 for i in range(m+1)]
p[0] = 1

for i in range(m):
    for index in range(i+1,-1,-1):
        if p[index] and s[index:i+1] in wordDict:
            p[i+1] = p[index]
            break