# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 21:12:07 2018

@author: Administrator
"""

s = "23"
dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
list1 = []
List = []


for i in s:
    list1.append(dic[i])
        
k = len(list1)

for a in list1[0]:
    if k == 1:
        List.append(j)
    else:
        for b in list1[1]:
            if k == 2:
                List.append(j+k)
            else:
                for c in list1[2]:
                    if k == 3:
                        List.append(a+b+c)
                    else:
                        for d in list1[3]:
                            if k == 4:
                                List.append(a+b+c+d)
                            else:
                                 for e in list1[4]:
                                    if k == 5:
                                        List.append(a+b+c+d+e)
                                    else:
                                        for f in list1[5]:
                                            if k == 6:
                                                List.append(a+b+c+d+e+f)
                                            else:
                                                for g in list1[6]:
                                                    if k == 6:
                                                        List.append(a+b+c+d+e+f)
                                                    