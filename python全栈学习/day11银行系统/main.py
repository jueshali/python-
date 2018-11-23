# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:38:04 2018

@author: LiPengcheng
"""


class Person():
    def __init__(self, id, password, money ):
        self.id = id
        self.__password = password
        self.__money = money
        self.__locked = 0

    def deposit(self, money):
        self.__money += money

    def withdraw(self, money):
        self.__money -= money

    def search(self):
        return self.__money

    def lock(self):
        self.__locked = 1

    def unlock(self):
        self.__locked = 0

    def checkpassword(self, password):
        if password == self.__password:
            return 1
        else:
            return 0

def main():
    dict1 = {}
    bankid = 1000
    while 1:
        str1 = input("请输入您的操作")
        if str1 == "quit":
            print("感想你的使用")
            break
        elif str1 == "search":
            temp_bankid = int(input())
            if dict1.get(temp_bankid):
                print(temp_bankid)
                search(dict1,temp_bankid)

            else:
                print("您输入的卡号有误")
        elif str1 == "creat":
            temp_id = input("请输入身份证号")
            temp_password = passwordcheck()
            if not temp_password:
                continue
            temp_money = 0
            temp_person = Person(temp_id, temp_password, temp_money)
            dict1[bankid] = temp_person
            bankid = bankid + 1
        else:
            continue










def creat():
    count = 3
    while 1:
        temp_id = input("请输入你的身份证号")



def passwordcheck():
    temp_password = input("请输入你的密码")
    if temp_password != input("确认你的密码"):
        temp_password = input("请输入你的密码")
        if temp_password != input("确认你的密码"):
            temp_password = input("请输入你的密码")
            if temp_password != input("确认你的密码"):
                print("密码错误次数过多")
                return False
            else:
                return temp_password
        else:
            return temp_password
    else:
        return temp_password


def search(dict1, temp_bankid):
    count = 3
    while 1:
        temp_password = input("请输入您的密码")
        if dict1[temp_bankid].checkpassword(temp_password):
            print(dict1[temp_bankid].search())
            break
        else:
            print("你输入的密码有误")
            if count == 0:
                print("密码错误三次")
                dict1[temp_bankid].lock()
                break
            count = count - 1











if __name__ == "__main__":
    main()


