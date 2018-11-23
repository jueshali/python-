# -*- coding: utf-8 -*-

from card import Card

class User(object):
    def __init__(self, name, idCard, phone, card):
        self.name = name
        self.idcard = idCard
        self.phone = phone
        self.card = card

