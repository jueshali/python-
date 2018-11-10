# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:10:59 2018

@author: Administrator
"""

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()