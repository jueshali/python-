# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 20:45:06 2018

@author: Administrator
"""

def is2mi(num):
    while num>=2:
        if num%2 == 1:
            return 0
        if num == 2:
            return 1
        num = num /2
    return 1

def zhezhishu(i):
   
    for j in range(2**i-1):
        if j%2 == 0:
            print("down")
        if j%2 == 1:
            print("up")
        if is2mi(j+2):
            print("\n")
        