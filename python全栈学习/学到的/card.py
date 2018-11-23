# -*- coding: utf-8 -*-

class Card(object):
    def __init__(self, card_id, card_password, money):
        self.card_id = card_id
        self.card_password = card_password
        self.money = money
        self.locked = False