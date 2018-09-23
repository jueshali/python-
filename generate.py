# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 15:32:29 2018

@author: Administrator
"""

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for i in fib(5):
    print i