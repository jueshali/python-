# -*- coding: utf-8 -*-
import random
from user import User
from card import Card
from admin import Admin

class Atm(object):
    def __init__(self, all_user):
        self.all_user = all_user


    def create_user(self):
        name = input("请输入您的姓名:")
        id_card = input("请输入您的身份证号码:")
        phone = input("请输入您的电话号码:")
        money = int(input("请输入预存款金额"))

        if money < 0:
            print("开户失败,预存款小于0")
            return -1

        password_one = input("请设置密码")

        # 验证密码
        if not self.check_password(password_one):
            print("密码输入错误，开户失败")
            return False

        card_id = self.random_card_id()

        temp_card = Card(card_id, password_one, money)
        temp_user = User(name, id_card, phone, temp_card)

        self.all_user[card_id] = temp_user
        print("你的卡号是%d" % card_id)
        print("开户成功")

    def search_user(self):
        search_card_id = int(input("请输入你要查询的卡号"))
        search_user = self.all_user.get(search_card_id)

        if not search_user:
            print("该卡号不存在")
            return False

        if search_user.card.locked:
            print("该卡已经被锁定")
            return False

        if not self.check_password(search_user.card.card_password):
            print("密码输入错误。查询失败")
            self.lock_user(search_card_id)
        else:
            print("账号: %s,   余额：%d" % (search_user.card.card_id, search_user.card.money))

    def withdraws(self):
        withdraw_card_user = self.get_opt_user()
        if withdraw_card_user:
            withdraw_card_money = int(input("请输入取款金额"))
            if withdraw_card_money > withdraw_card_user.card.money:
                print("超过你所要取款的金额")
                return False
            else:
                withdraw_card_user.card.money -= withdraw_card_money
                print("取款成功")
                return True
        else:
            return False

    def save_money(self):
        withdraw_card_user = self.get_opt_user()
        if withdraw_card_user:
            withdraw_card_money = int(input("请输入存款金额"))
            if withdraw_card_money < 0:
                print("取款不能为负数")
                return False
            else:
                withdraw_card_user.card.money += withdraw_card_money
                print("存款成功")
                return True
        else:
            return False

    def transfer_money(self):
        print("请输入转出账户")
        out_user = self.get_opt_user()
        print("请输入转入账户")
        in_user = self.get_opt_user()
        temp_money = int(input("请输入转账金额"))
        if temp_money < 0:
            print("金额不能为负！")
            return False
        if temp_money > out_user.card.money:
            print("金额超出所要转的金额")
            return False
        out_user.card.money -= temp_money
        in_user.card.money += temp_money
        print("转账成功")

    def change_password(self):
        change_password_user = self.get_opt_user()
        if change_password_user:
            change_password_user.card.card_password = input("请输入你要修改的密码")
            print("密码修改成功")
        else:
            return False

    def lock_user(self, card_id=None):
        if card_id:
            print("该卡锁定")
            lock_user = self.all_user.get(card_id)
            lock_user.card.locked = True
        else:
            lock_card_id = int(input("请输入你要锁定的卡号"))
            lock_user = self.all_user.get(lock_card_id)
            if not lock_user:
                print("该卡号不存在")
                return False
            else:
                if not self.check_password(Admin.password):
                    print("管理员密码多次错误")
                else:
                    print("该卡锁定！")
                    lock_user.card.locked = True

    def unlock_user(self):
        lock_card_id = int(input("请输入你要锁定的卡号"))
        lock_user = self.all_user.get(lock_card_id)
        if not lock_user:
            print("该卡号不存在")
            return False
        elif not lock_user.card.locked:
            print("该卡未被锁定")
            return True
        else:
            if not self.check_password(Admin.password):
                print("管理员密码多次错误")
            else:
                lock_user.card.locked = False
                print("解锁成功")

    def new_card(self):
        new_user = self.get_opt_user()
        del self.all_user[new_user.card.card_id]
        new_card_id = self.random_card_id()
        new_user.card.card_id = new_card_id
        self.all_user[new_user.card.card_id] = new_user

    def kill_user(self):
        kill_user = self.get_opt_user()
        del self.all_user[kill_user.card.card_id]
        print("销户成功")

    def check_password(self, real_password):
        for i in range(3):
            temp_password = input("请输入密码")
            if temp_password == real_password:
                return True
            else:
                print("请重新输入")
        return False

    def random_card_id(self):
        while True:
            temp_card = random.randint(1000, 9000)
            if not self.all_user.get(temp_card):
                return temp_card

    def get_opt_user(self):
        withdraw_card_id = int(input("输入卡号"))
        withdraw_card_user = self.all_user.get(withdraw_card_id)

        if not withdraw_card_user:
            print("该卡号不存在")
            return False

        if withdraw_card_user.card.locked:
            print("该卡已经被锁定")
            return False

        if not self.check_password(withdraw_card_user.card.card_password):
            print("密码输入错误。查询失败")
            return False
        else:
            return withdraw_card_user

    def user_check(self):
        print(self.all_user)
