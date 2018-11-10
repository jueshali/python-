# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 15:44:52 2018

@author: Administrator
"""

s = [["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]

def change(self,i,j,s):
    if i < 0 or j < 0 or i >len(s) or j > len(s[0]):
        return 
    if s[i][j] == "1":
        s[i][j] == "0"
    self.change(i+1,j,s)
    self.change(i-1,j,s)
    self.change(i,j+1,s)
    self.change(i,j-1,s)
        
temp_s = s
count = 0
a = range(len(s))
b = range(len(s[0]))
for i in a:
    for j in b:
        if s[i][j] == "1":
            count = count +1
            self.change(i,j,s)
            



