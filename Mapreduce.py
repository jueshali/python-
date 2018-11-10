# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 20:37:15 2018

@author: Administrator
"""

doc = {
       0:"Deer Bear River",
       1:"Car Car River",
       2:"Dear Car Bear",
}

class map_reduce(object):
    def __init__(self,k):
        self.k = k
        self.sample = {}
        
    def EmitIntermediate(self,word):
        self.sample[word] = self.k
        
    def Map(self,v):    
        for each in v.split(" "):
            self.EmitIntermediate(each)
    def Reduce():
        result = 0
        for each in sample:
            result += sample[each]