# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:38:04 2018

@author: Administrator
"""


# 元组元素访问
# 下标从0开始
# 取值
# 元组一旦初始化就不能修改了
print("**************")
tuple4 = (1,2,3,4)
print(tuple4[0])
print(tuple4[-1])


# 可以在元组中存储数组，这样也可以修改
print("**************")
tuple5 = (1,2,3,4,[1,3,4])
tuple5[-1][0] = 500

# 通过del删除
print("**************")
tuple6 = (1,2,3)

del tuple6


# 元组操作
print("**************")
tuple7 = (1,2,3)
tuple8 = (4,5,6)

tuple9 = tuple7+tuple8

tuple10 = tuple7*3

# 判断元素是否在元组中
print("**************")
t11 = (1,2,3)
print(1 in tuple10)

# 元组的截取
# 格式：元组名[3:7]从3截取到7
print("**************")
print(t11[1:3])

# 二维元组：元素为一维元组的元组
print("**************")
t13 = ((1,2,3),(4,5,6),(7,8,9))
print(t13[1][1])


# 元组的方法
t14 = (1,2,3,4,5,6)

# len()返回元组中元素的个数,max(),min()
print("**************")
print(len(t14))


# 将列表转为元组
print("**************")
list15 = [1,2,3]

t15 = tuple(list15)
print(t15)

# 元组就是不可变的列表，安全，别人修改不了

print("**************")
str38 = "sunk**is******good**man*"


# split()
print(str38.split("*",3))  #split方法以第一个参数为分割符号，截取第二个int参数个，剩下的都一起丢出来。

for s in str38.split("*"):
    if len(s)>0:
        print(s)
print("**************")        
# splitlines([keepend]) 按照'\r','\r\n',\n分割返回   [函数中有中括号说明可写可不写]
# keepend为True时会保留空行符号
str40 = """hello world
hello you 
hello me
"""

print(str40.splitlines(True))  
print("**************")
# join() 以指定的字符串分隔符号，将其组合成一个字符串
list41 = ['sunk', '', 'is', '*****good**man*']

str42 = "".join(list41)

print("**************")
# max(),min() 按照ASCII 嘛求大小


# replace(olderstr,newstr,count) 用newstr代替olderstr，默认全部替换，指定count那么只指定前count个
str44 = "sunck is a good man"

str45 = str44.replace("good","nice")

print(str44,str45)
print("**************")
# 创建一个字符串映射表
#           反射表要转换的字符串，目标字符串
# t46 = str.mro("sunck","kaige")    #将s~k,u~a,n~i...

str47 = "sunck is a good man"

# str48 = str47.translate(t46)
# startswith(str,start,end=len(str)) 判断是否以str开始，从start开始计数（默认为0）
# endwith判断指定范围是否以str结尾
print("**************")
str49 = "sunck is a good man"
print(str49.startswith("sunck"))

print(str49.startswith("sunck",5,10))

str50 = "sunck is a good man"
print(str50.endswith("man",5))


# encode(encoding="utf-8",errors ="strict")
print("**************")

str51 = "sunck is a good man"
data52 = str51.encode()
print(str51.encode())
print("**************")
# 解码码：注意：要与编码时的编码格式一致一致error ignore不考虑错误
str53 = data52.decode("utf-8")
print(str53)
print("**************")
# isalpha() 如果字符串中有一个字符，且所有字符都是字母，返回True,不然返回Flase

print("**************")
str54 = "sunck is a good man"
print(str54.isalpha())
# isalnum()   字符串至少有一个字符，判断是否完全由数字和字母组成
# isupper() 字符串至少有一个英文字符，且所有字符都是大写字母，返回True,除了英文字符以外的不管，如果没有英文字符返回False

# islower() 字符串中至少有一个英文字符，且所有的字符都是小写,如果没有英文字符返回False
print("abcd#".islower())
print("**************")
# istitle() 如果字符串是标题话的返回True
# isdigit() 如果字符串只包含数字字符，返回True
print("123".isdigit())
print("**************")

# isdecimal()字符串只包含十进制字符
# isspace()字符串只包含空格字符
print("**************")
print(" ".isspace())
print("\n".isspace())
print("\r".isspace())
print("\t".isspace())

"""
概述：
使用键-值存储形式，具有极快的查找速度
key的特性：
1:字典中key必须唯一
2：key必须是不可变的对象（字符串，整数），list不能作为Key,一般将字符串作为KEY

注意字典是无序的

思考：保存多位学生的姓名和成绩

使用字典，学生姓名为key，学生成绩为值

"""
print("**************")
# 获取： 字典名[key],或者dict.get()
print("**************")
dict1 = {"lilei": 23, "zhangsan": 80, "lisi": 72}
print(dict1["lilei"])
print(dict1["lisi"])

print(dict1.get("wangwu"))
print("**************")
# 添加：注意key值不能与已有重复，不然会修改，即有则修改，无则增加。
dict1["lipengc"] = 100
print(dict1.get("lipengc"))

# 删除：

dict1.pop("lisi")
print("**************")
# 遍历
for key in dict1:
    print(key)

print(dict1.values())

for value in dict1.values():
    print(value)

# dict1.items返回的是一个元组
for k,v in dict1.items():
    print(k, v)

# enumerate()里面放一个枚举对象
for i,v2 in enumerate(dict1):
    print(i, v2)

# 和list比较
# 1、查找插入的速度非常快，不会随着N的增加而变慢
# 2、需要占用大量内存


