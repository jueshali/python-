# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:38:04 2018

@author: LiPengcheng
"""

"""
name:wife
format:sex,name,age,height,weight,face_value
function:cook, wash, 

name:husband, 
format:sex, age, height weight  
function:color type

"""
"""
design a class 
class name the first letter capital
class format
class function

object don't use memory ,it's a type of data Struct
class use it

class name(father object[can have many]):
object is a basic object
"""


class People(object):   # defind format
    name = ""
    age = 0
    height = 0
    weight = 0

    # defination function
    # notice the function must have a self as it's first argument
    # self refer a class
    def run(self):
        print("I'am running")

    def eat(self, food):
        print("eat" + food)

    def open_door(self):
        print("我已经打开了冰箱门")

    def put_in(self):
        print("我已经把大象装进去了")

    def close_door(self):
        print("门已经被关闭了")


"""
实例化对象
格式： 对象名 = 类名（参数列表）
注意： 没有参数，小括号也不能省略
"""


people1 = People()
print(people1)   # 打印出得是这个类得地址


people2 = People()
print(people2)
people2.run()

# 对象在堆区，变量在栈区
# 世界上没有两个一模一样得对象


# 使用对象
people1.name = "zhangsan"
people1.age = 10
people1.height = 10
people1.weight = 10
people1.run()
people1.open_door()
people1.put_in()
people1.close_door()
people1.eat("橘子")
print(people1.weight, people1.height, people1.name, people1.age)

"""
访问方法
格式：对象名.方法名（参数列表）
"""


# 目前所有创建得对象属性都是一样得

class People(object):   # 构造对象得初始状态
    name = ""
    age = 0
    height = 0
    weight = 0

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def run(self):
        print("I'am running")

    def eat(self, food):
        print("eat" + food)


"""
通过__init__方法实现 在使用类创建对象得时候调用
如果不显示得写出构造函数，会默认添加一个空得构造函数
"""

people1 = People("sda", 10, 20, 30)

print(people1.name, people1.age, people1.height)


"""
self 代表类得示例，而非类，哪个对象调用方法，那么该方法中得self就代表那个对象
self.__class__代表类名

"""


class People(object):   # 构造对象得初始状态
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def run(self):
        print("I'am running")
        print(self.__class__)
        p = self.__class__("tt", 90, 20, 20)
        print(p)

    def eat(self, food):
        print("eat" + food)

    def introduce(self):
        print("Hello %s , %d" % (self.name, self.age))

    # 析构函数
    """

    析构函数：__del__() 释放对象时自动调用，堆区的内容需要手动释放，对象释放后就不能再访问了

    """

    def __del__(self):
        print("这是一个析构函数")




people1 = People(10,1,3,3)
people1.introduce()
people1.run()


def fun():
    per1 = People("1",1,2,3)

# 在函数里定义的对象会在函数结束时自动释放，减少内存空间的浪费
fun()


# __repr__ 与__str__
"""
重写：将函数重新定义写一遍
__repr__()：给机器用的，在Python解释器（黑屏终端）中直接敲对象名再回车后调用的方法，
__str__():调用print对象时自动调用,是一个描述对象的方法。
当一个对象的属性很多，并且都需要打印时，可以重写__str__方法
"""

class People4(object):   # 构造对象得初始状态
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        print("你在打印对象吗")
        return 0


per1 = People4("asd", 1, 3, 4)
print(per1.name, per1.age, per1.height)

print(per1.__sizeof__())


class Person():
    def __init__(self, count, name):
        self.bullet = count
        self.name = name

    def shoot(self):
        self.bullet = self.bullet - 1

    def bullet_left(self):
        print(self.bullet)


gunman = Person(10, "张三")

while gunman.bullet > 0:
    gunman.shoot()
    gunman.bullet_left()
