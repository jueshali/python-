# -*- coding: utf-8 -*-
"""
Created on  Nov 14 09:38:04 2018

@author: 李鹏程
"""
import collections
import os
import time


# use a list to simulate a stack

stack = list()

# push
stack.append("A")

# pop
res = stack.pop()

# queue

queue = collections.deque()

print(queue)

queue.append("A")

print(queue)

print(queue.pop())


# check dir recursive
Path = r"C:\Users\Administrator\Desktop\study\python学习"


def get_file(path, list1=[]):
    fileslist = os.listdir(path)
    for filename in fileslist:
        temp = os.path.join(path, filename)
        if os.path.isdir(temp):
            get_file(temp, list1)
        else:
            list1.append(temp)
    return list1


print(len(get_file(Path)))

print("*******************************8")
# stack get file


def get_file2(path):
    list2 = list()
    list3 = list()
    list2.append(path)
    while list2:
        temp = list2.pop()
        filelist = os.listdir(temp)
        for filename in filelist:
            temp1 = os.path.join(temp, filename)
            if os.path.isdir(temp1):
                list2.append(temp1)
            else:
                list3.append(temp1)
    return list3


print(len(get_file2(Path)))


# queue get file


def get_file3(path):
    list1 = collections.deque()
    list1.append(path)
    list2 = list()
    while list1:
        temp = list1.popleft()
        filelist = os.listdir(temp)
        for filename in filelist:
            temp1 = os.path.join(temp, filename)
            if os.path.isdir(temp1):
                list1.append(temp1)
            else:
                list2.append(temp1)
    return list2


print(len(get_file3(Path)))


"""
UTC(世界协调时间)，China utc+8

time format:
1、时间戳   int+float to display time use second as time, it means how long have been left since 1970.1.1
2、tuple     a tuple with nine int value(year,month,hours,minutes,seconds,weekday,Julia day,DST(1or-1or0))
3、format string     %Y year
"""
c = time.time()

# 将时间戳转为UTC时间元组
nowtime = time.gmtime(c)

b = time.localtime(c)
print(b)

# 将元组表示得时间表示为时间戳
m = time.mktime(b)
print(m)

# 将时间元组转换为字符串












