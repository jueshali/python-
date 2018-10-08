# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 19:54:27 2018

@author: Administrator
"""
"""
括号匹配
"""
needle = "ll"
haystack = "hello"


if needle == "":
     b = 0
        
length1 = len(needle)
length2 = len(haystack)

k = 0
j = length1-1
        
while j < (length2-1):
    if haystack[k] == needle[0]:
        if haystack[k:j+1] == needle:
            c = k
    k = k+1
    j = j+1
    
        