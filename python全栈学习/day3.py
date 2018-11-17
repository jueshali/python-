# -*- coding: utf-8 -*-
"""
Created on  Nov 14 09:38:04 2018

@author: 李鹏程
"""

# Data intensive
import functools
"""
Decorator : use function as a argument and return a function to replace it.a function that
return function
"""


def func1():
    print ("sunk is a good man")


def outer(func):
    def inner():
        func()
        print("I'm a decorator")
    return inner


# complex decorator,with parameter


def outer1(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)
    return inner


@outer1     # like say = outer1(say)
def say(age):
    print("sunck is %d years old" % (age))

# change function without change source old


# Universal decorator

def outer3(func):
    def inner(*args, **kwargs):
        # the function you want add
        func(*args, **kwargs)
    return inner


# Partial function

def int2(str1, base=2):
    return int(str1, base)


print(int2("10011"))


# set a parameter to produce a new function and make it can't change

int3 = functools.partial(int, base=2)

"""
Scope of the variable: where the variable can been call
The access rights depend on the location of the variable
scope type:  location scope
             global scope
             built in scope
"""


# exception handling
# when program facing problem,it continue running
"""
try......except....else
format:
try:
    statement t
expect wrong code as e:
    statement 2
expect wrong code as e:
    statement 2
expect wrong code as e:
    statement 3
else:
    statement e    

else is not necessary

function : test if the statement t has any wrong

logic:

"""

try:
    print(3/1)
except ZeroDivisionError as e:
    print("you divide zero")
except NameError as e:
    print("Name wrong")
else:
    print("No wrong")


print("123")

# use except and don't use ant wrong statement

try:
    print(3/0)
except:
    print ("wrong")

# use try to get many wrong
try:
    pass
except(NameError,ZeroDivisionError):
    print ("something wrong")


"""
especial: error is a class
1、baseexception : base error can't put it in the first place , because it run in a order way
                all error inherited from the baseexception
                
2、Multi-layer call:ex:main call fun2 fun2 call fun1 , when main() raise a error , we will get it 
"""


def func1(num):
    print(1/num)


def func2(num):
    func1(num)


def main():
    func2(0)


try:
    main()
except ZeroDivisionError as e:
    print("find the error")

"""
try:
except:
finally:
    statement f 
f run in any way
"""


# assert
def func(num, div):

    assert (div != 0), "div不能为0"
    return num/div


