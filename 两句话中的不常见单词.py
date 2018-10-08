# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 19:15:48 2018

@author: Administrator
"""

A = "this apple is sweet"
B = "this apple is sour"
A = A.split(" ")
B = B.split(" ")
C = []
if len(A) <= len(B):
    for s in A:
        if s in B:
            num = B.count(s)
            for i in range(num):
                B.remove(s)
        else:
            C.append(s)
for s in B:
    C.append(s)