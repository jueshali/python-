# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 11:17:28 2018

@author: Administrator
"""

class HEAP(object):
    def __init__(self,high,maxnum):
        self.list = []
        self.high = high
        self.heapsize = 0
        self.maxnum = maxnum
        self.i = 0
    def MAXHEAPIFY(self,List,i):
        self.list = List
        self.heapsize = len(self.list)
        l = self.LEFT(i)
        r = self.RIGHT(i)
        if l<= self.heapsize and self.list[i]<self.list[l]:
            lagest = l
        else:
            lagest = i
        if r<= self.heapsize and self.list[i]<self.list[r]:
            lagest = r
        if lagest != i:
            self.list[i] = self.list[lagest]
            self.MAXHEAPIFY(self.list,lagest)
    def LEFT(self,i):
        return 2*i
    def RIGHT(self,i):
        return 2*i+1