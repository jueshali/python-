# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 20:40:01 2018

@author: Administrator
‘从2三.二习月个等概率随机产生I一5的随机函数rand I Tas如F工e七日川(川l匕)(M:{卜.肠曰「巾山()    
除此之外，耳、能使川fr_f}}l额外i I'o随机机}i}}l
.请川，-and I Toy实现等概率随机，I}}f }oLr-}a数rind 1 To7-!一7的


"""
import random

def rand5():
    return random.randint(1,5)


def  rand7():
    num = 30
    
    while num > 20:
        num = (rand5()-1)*4+(rand5()-1)
    return num%7+1