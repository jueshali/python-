# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:38:04 2018

@author: Administrator
"""
import time
import datetime
import calendar
import mypack
from mypack import my_sum
from mypack import *

d1 = datetime.datetime.now()
print(d1)

d2 = datetime.datetime(1999,10,1,10,28,25,123456)
print(d2)

# translate datetime to str
d3 = d1.strftime("%Y-%m-%d %X")
print(d3)

# translate str to datetime,the two arguement must have same format
d4 = datetime.datetime.strptime(d3, "%Y-%m-%d %X")
print(d4)

# minus time
d5 = datetime.datetime.now()


#time.sleep(5)

d6 = datetime.datetime.now()

d7 = d6 - d5

print(d7)

#
d8 = d7.days

"""
Calendar module
"""

# use , return a calendar

print(calendar.month(2017, 7))

# judge leap year
print(calendar.isleap(2000))

# return the first weekday of that month and the amount of that days
print(calendar.monthrange(2017, 7))

# return the index of day
print(calendar.monthcalendar(2018, 11))


mypack.mypack()




"""
from import
from module import name1,[name2],
only import some of the module

disadvantage  will cover the same name moudle


from module import *
import all , not recommder
"""


b = my_sum(2, 3)
my_pack()
print(b)


"""
__name__: module is a executable file with .py,a module using by another file
use __name__ to make  some of the function don't call in module,every python file has a __name__,
when __name__ == __main__
如果当前文件为入口文件时__name__ == __main__，否则作为模块被调用
"""


"""
package
deal with the problem that module with same name 

only with the __init__ file can recognize as a package
"""



"""
pip install pollow
"""

"""
im = Image.open("file")
print(im.format, im.size, im.mode)

"""


























