# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:38:04 2018

@author: LiPengcheng
"""


import time

class Admin(object):
    admin = "1"
    password = "1"

    def printAdminView(self):
        print("***************************************************")
        print("*                                                 *")
        print("*                                                 *")
        print("*                     欢迎登录银行                  *")
        print("*                                                 *")
        print("*                                                 *")
        print("***************************************************")

    def admin_option(self):
        admin = input("请输入管理员账号")
        if self.admin != admin:
            print("账号输入有误")
            return False
        password = input("请输入管理员密码")
        if self.password != password:
            print("密码输入有误")
            return False

        # 账号密码正确

        time.sleep(2)
        return True

    def printsysView(self):
        print("***************************************************")
        print("*     开户(1)                查询(2)               *")
        print("*     取款(3)                存款(4)               *")
        print("*     转账(5)                改密(6)               *")
        print("*     锁卡(7)                解锁(8)               *")
        print("*     补卡(9)                销户(0)               *")
        print("*                                                 *")
        print("*                退出（q）                         *")
        print("***************************************************")
