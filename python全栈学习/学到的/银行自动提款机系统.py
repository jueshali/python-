# -*- coding: utf-8 -*-
"""
人：Person
属性：姓名。 身份证号  电话号 卡



卡：
类名：Card
属性：卡号 密码 余额
行为：管理员界面， 管理员登录， 系统功能界面

提款机：
类名：ATM
属性：
行为：开户 查询 取款 存储 转账 改密 锁定 解锁 补卡 销户 退出



界面类：
类名：admin
属性：
行为：管理员界面， 管理员登录， 系统功能界面, 管理员退出



"""
from admin import Admin
from atm import Atm
from card import Card
from user import User
import pickle
import os

import time


def main():

    # 界面对象
    view = Admin()

    # 管理员开机
    view.printAdminView()
    if not view.admin_option():
        return -1

    print("登录成功！请稍后")

    # 存储所有用户的信息
    abs_path = os.getcwd()
    file_path = os.path.join(abs_path, "allusers.txt")

    with open(file_path, "rb") as f:
        all_user = pickle.load(f)

    ATM = Atm(all_user)


    view.printsysView()

    while True:
        # 等待用户操作
        view.printsysView()
        option = input("请输入您的操作：")
        if option == "1":
            # 目标向用户字典中增加（卡号———用户）
            ATM.create_user()

        elif option == "2":
            ATM.search_user()

        elif option == "3":
            ATM.withdraws()

        elif option == "4":
            ATM.save_money()

        elif option == "5":
            ATM.transfer_money()

        elif option == "6":
            ATM.change_password()
        elif option == "7":
            ATM.lock_user()

        elif option == "8":
            ATM.unlock_user()

        elif option == "9":
            ATM.new_card()

        elif option == "0":
            print("销户")

        elif option == "q":
            if view.admin_option():
                print("退出，成功")
                # 将当前系统中的文件保存进入文件中
                with open(file_path, "wb") as f:
                    pickle.dump(ATM.all_user,f)
                return True

            else:
                print("退出失败,请重新退出")
                time.sleep(1)
        elif option == "c":
            ATM.user_check()
        time.sleep(2)








if __name__ == "__main__":
    main()