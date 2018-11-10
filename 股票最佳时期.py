# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 16:20:07 2018

@author: Administrator
"""

prices = [7,1,5,3,6,4]

pmin = prices[0]
valmax = 0

for i in prices: 
    valmax = max(valmax,i-pmin)
    pmin = min(i,pmin)
    