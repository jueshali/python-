# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 09:38:04 2018

@author: 李鹏程
"""
# import time 导入时间包


timeStr = "11:11:11"

time = timeStr.split(":")


def splus(s, timesype):
    """
    :param s: 输入一个时间字符
    :return:  返回该时间加一秒
    :param timesype:输入时间的type
    """
    if timesype == 's':
        if s == "59":
            return "0"
        else:
            return str(int(s)+1)
    if timesype == 'h':
        if s == "24":
            return "0"
        else:
            return str(int(s)+1)


if time[2] == "59":
    if time[1] == "59":
        time[1] = splus(time[1], "s")
        time[0] = str(int(time[0])+1)
    else:
        time[1] = splus(time[1], "s")

time[2] = splus(time[2], "s")

timeStr = ":".join(time)

print(timeStr)


print("****************")

"""
set 类似dict，是一组key集合，不存储value
本质：无序和无重复元素的集合
"""
# 创建
# 创建set需要一个list或者tuple,dict作为输入集合

s1 = set([1,2,3,4,3])

print(s1)



