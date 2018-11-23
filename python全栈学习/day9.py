# -*- coding: utf-8 -*-
"""
Created on  Nov 14 09:38:04 2018

@author: 李鹏程
"""
import types

class People4(object):   # 构造对象得初始状态

    def __init__(self, name, age, height, weight, money):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.__money = money

    def balance_inquiry(self):
        return self.__money

    def add_money(self, num):
        self.__money = self.__money + num


per1 = People4("asd", 1, 3, 4, 10)
per1.age = 10

# 如果要让内部的属性不被外部直接访问，在属性前加两个下划线（__）,python在属性前加
# 属性就变成了私有属性。


# print(per1.__money)
per1.a = 100
print(per1.a)

# 下面这个语句并没有改变__money这个值
per1.__money = 100
print(per1.balance_inquiry())

# 通过内部的方法修改内部属性，同时还可以通过方法进行数据的过滤
# 通过内部方法才能获得私有变量
per1.add_money(100)
print(per1.balance_inquiry())

# 不能直接访问__money是因为python解释器把__money变成了_Person__money,不同版本的解释器存在
# 不能解释器解释的变量名不一致
# print(per1._People4__money)

# 在python中_XXX变量，这样的实例变量外部是可以访问的，但是按照约定的规则，
# 当我们看到这样的变量时意思是“虽然我可以被访问，但是请把我是为私有变量，不要直接访问”


class People(object):
    def __init__(self, gun):
        self.gun = gun

    def fire(self):
        if self.gun.clip.bulletCount == 0:
            print("没有子弹了")
        else:
            self.gun.shoot()
            print(self.gun.clip.bulletCount)

    def add_bullet(self, num1=1):
        self.gun.clip.add_bullet(num1)


class Gun(object):
    def __init__(self, clip):
        self.clip = clip

    def shoot(self):
        self.clip.bulletCount -= 1


class Clip(object):

    def __init__(self, bullet_count):
        self.bulletCount = bullet_count

    def add_bullet(self, num):
        self.bulletCount += num


a = Clip(9)

b = Gun(a)

c = People(b)

c.fire()
c.fire()

c.fire()
c.add_bullet(3)
c.fire()


# 继承，有两个类A，B。当我们说A类继承自B类的时候，那么A类就拥有了B类的中的属性和方法。
# 继承者称之为子类，被继承者称之为父类。
"""
1、简化代码，减少冗余
2、提高了代码的健壮性
3、修改父类，就可以修改所有的子类
4、提高了代码的安全性，
5、是多态的。
缺点：耦合和内聚是描述类与类之间的关系的。耦合：类之间的联系
内聚，能干的活越多。
违背了高内聚，低耦合。
"""


class Women_people(People):
    pass


b = Women_people(b)
b.fire()


# 继承，单继承。子类可以拥有一些自己独有的属性。父类中的私有属性只能通过父类继承来的公有方法才能取值和赋值。


class Parent(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("run")


class Student(Parent):
    def __init__(self, name, age, id1):
        super(Student, self).__init__(name, age)
        self.id = id1


student_1 = Student("zhangsan", 10, 1)

print(student_1.name)
student_1.run()




class Father(object):
    def __init__(self, money):
        self.money = money

    def play(self):
        print("play")

    def func(self):
        print("父类")


class Mother(object):
    def __init__(self, face_value):
        self.face_value = face_value

    def play(self):
        print("play")

    def func(self):
        print("母类")


class Child(Father, Mother):
    def __init__(self, money, face_value):
        # 多继承
        Father.__init__(self, money)
        Mother.__init__(self, face_value)
        self.height = 10


def main():
    c = Child(100, 300)
    print(c.money, c.face_value, c.height)
    c.func()            # 父类中的方法名相同时，默认调用括号里面的第一个


if __name__ == "__main__":
    main()




"""
多态:一种事物的多种形态。继承是多态的前提。

最终目标：实现人可以喂任何一种动物
"""
# 定义一个人类可以喂猫和老鼠吃东西

class Person(object):
    """
    def feed_cat(self, cat):
        print("给你食物")
        cat.eat()
    def feed_mouse(self, mouse):
        print("给你食物")
        mouse.eat()
    """
    def feed_animal(self, animal):
        print("给你食物")
        animal.eat()



class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s eat" % self.name)


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)


class Mouse(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)


tom = Cat("tom")
jerry = Mouse("jerry")

man1 = Person()
# man1.feed_cat(tom)
# man1.feed_mouse(jerry)
man1.feed_animal(tom)
man1.feed_animal(jerry)


"""
对象属性和类属性
"""

class Person(object):
    name = "Person"                   # 在这里的是类属性：用类名来调用的属性
    def __init__(self, name):         # 在这里的是对象属性
        self.name = name

peter = Person("peter")
print(peter.name)

# 如果删除对象属性后，就可以访问到雷属性。
del peter.name
print(peter.name)
# 如果类和对象属性都存在，那么优先访问对象属性。因此最好不要让类属性和对象属性重名。
peter.age = 10

# 动态的给对象添加属性，对于类创建的其他对象没有作用，
print(peter.age)


# 动态的给对象添加属性，对于类创建的其他对象没有作用，

class Person(object):
    __slots__ = ("name", "age", "speak")

per1 = Person()

per1.name = "tom"
print(per1.name)

# 动态添加方法 ,类似于一个偏函数，将per1这个参数给固定
def say(self):
    print("my name is " + self.name)

per1.speak = types.MethodType(say, per1)

per1.speak()


# 如果想要限制实例的属性，
# 比如直线让per1添加特定的一些属性。

# 再定义类时定义一个特定的属性（__slots__）,一个元组
class Person10(object):
    def __init__(self, age):
        self.__age = age          # 限制访问
    @property                    # 取值时使用的这个方法
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age<0:
            age = 0
        self.__age = age



# 属性直接对外暴露，数据不安全，而且没有数据过滤。
# 当被限制时，使用set和get方法,
# peoperty 可以让受限制的属性获得。

per2 = Person10(10*56)

per2.age = -100

print(per2.age)


# 运算符重载，不同的类型用加法会有不同的解释。
class Person11(object):
    def __init__(self, num):
        self.num = num

    def __add__(self, other):  # self 加号前，Other加号后
        return Person11(self.num + other.num)

    def __str__(self):
        return "num=" + str(self.num)



person1 = Person11(1)
person2 = Person11(2)

print(person1 + person2)           # per1 + per2 == per1.__add__(per2)





