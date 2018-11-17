# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 09:38:04 2018

@author: 李鹏程
"""
# import time 导入时间包
from collections import Iterable
from collections import Iterator

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

s1 = {1, 2, 3, 4, 3}

# 不能存不能作为key的值（可变的不能作为key，例如list是可变的，元组可以作为key），可以添加重复的但是不会有效果

print(s1)
s5 = {1, 2, 3, 4}

s5.add(9)

# s5.add([1, 3])
# update()方法可以将数组插入，建数组打碎后插入
s5.update([3, 5, 6])
print (s5)

# 删除
s6 = {1, 2, 3, 4}
s6.remove(2)
print (s6)

# set是没有索引的。可以通过遍历从set中取值,过滤元素用，里面不会重复存储元素
print("******************")
for inx,val in enumerate(s6):
    print(inx,val)

s8 = {1, 2, 3}
s9 = {2, 3, 4}

s10 = s8 & s9

s11 = s8 | s9

print ("交集", s10)
print ("并集", s11)

# set ->list
l9 = list(s9)
t10 = tuple(s10)

# 迭代器

"""
可迭代对象： 可以直接作用于For循环的对象统称为可迭代对象
（iterable），we can use isinstance()to figure out sth if something is iterable
1, collection data type : list tuple dict  set string
2, generator , include generators or generator function with yield
"""

print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print (isinstance((x for x in range(10)),Iterable))
"""
Iterable: not only use in the for loop,but also can called by next() and return the next value.at last 
it will raise a error type StopIteration

iterator : a object than can Called by function next() and return next value
we can use isinstance()to figure out  if something is iterator
"""


print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance({}, Iterator))
print (isinstance((x for x in range(10)), Iterator))

l = (x for x in range(10))

print (type(l))

# translate sth to iterator
l3 = [1, 23, 4, 5]
iter1 = iter(l3)

print("******************")


def myprint():
    """
    :return: no return
    """
    print("this is a function with no parameter")


"""
format: name(parameters)
name: when you want use the function , you should type it's name
parameters: the function user translate the information to function

the nature of the function is the process that Arguments  parameters  parameter
"""


# must Enter parameters in order
# return value

def sum1(num1, num2):
    return num1 + num2

# give the result to function caller
# when function Execution return statement ,the function is end


sum1 = sum1(1, 2)
print(sum1)


"""Passing parameters
1: passing value:passing sth that is unchangable type
"""


def func1(num1):
    num1 = 10


temp = 20
func1(temp)
print(temp)

"""
2: Reference pass:passing changeable type

"""


def func2(list1):
    list1[0] = 100


list2 = [1, 2, 3]
func2(list2)
print(list2)

# a storage the address of 10
a = 10
b = 10
print(id(a), id(b))
a = a + 10
print(id(a), id(b))


# Keyword arguments allow us don't need to enter arguments in order
# use Keyword arguments

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 09:38:04 2018

@author: 李鹏程
"""
import operator
# default parameter: when yon call a function ,if you don't set any parameter ,the function use default parameter
# it's better to use default parameter in the last location


def my_print(str1 = "I can do ", str2 = "it"):
    print(str1,str2)


# Indefinite length parameter: deal more parameter than  the number of function initial defined

# the parameter with * can store all the unnamed arguments. the parameter with * is a tuple type


def func(name, *arr):
    print(name)
    for x in arr:
        print(x)

# key word parameter ,store in a dict type, and when you call this function ,you should in a key parameter way(like x=1)


def my_sum(*num):
    sum1 = 0
    for i in num:
        sum1 = sum1 + i
    return sum1


def func2(**kwargs):
    print(kwargs)
    print(type(kwargs))


def func3(*args,**kwargs):
    pass


"""
# anonymous functions: define a function without using "def" ,but use lambda

feature:
1、it's a expression ,simple than def way
2、it's body is a expression ,not a code block,
3、lambda has namespace just belong to itself and it can't use the parameter in a casual way.

format: lambda arguments1,arguments2,..:expression
"""


# use the function in operator to replace lambda


operator.add(5, 6)
