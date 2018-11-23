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

