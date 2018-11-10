# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:48:10 2018

@author: 李鹏程 Dmir

一个简单的蓄水池算法运行于python 2.7
"""
import random

class ReservoirClassic(object):
    """
       定义一个蓄水池类
       接受一个参数max_size作为水池大小
       sample存放样本
       add方法用于处理流数据
       reset方法用于将水池清空
    """
       
    def __init__(self,max_size):
        self.samples = []
        self.max_size = max_size
        self.i = 0
    
    def add(self,element):
        size = len(self.samples)
        if size < self.max_size:
            self.samples.append(element)
        else:
            j = random.randint(0,self.i)
            if j < size:
                self.samples[j] = element
        self.i +=1
    def reset(self,max_size):
        self.samples = []
        self.max_size = max_size
        self.i = 0
        
K = 3
a = ReservoirClassic(K)
print("input end to stop")
countnum = [0,0,0,0,0,0]
for i in range(0,100000):
        a.add("ball1")
        a.add("ball2")
        a.add("ball3")
        a.add("ball4")
        a.add("ball5")
        a.add("ball6")
        countnum[0]= countnum[0]+a.samples.count("ball1")
        countnum[1]= countnum[1]+a.samples.count("ball2")
        countnum[2]= countnum[2]+a.samples.count("ball3")
        countnum[3]= countnum[3]+a.samples.count("ball4")
        countnum[4]= countnum[4]+a.samples.count("ball5")
        countnum[5]= countnum[5]+a.samples.count("ball6")
        a.reset(K)
