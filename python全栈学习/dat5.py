# -*- coding: utf-8 -*-
"""
Created on  Nov 14 09:38:04 2018

@author: 李鹏程
"""
import os
import win32gui
import win32con
import win32com
import win32api
import time
import win32process
import ctypes
"""
include all the system operation 

"""
"""
PATH = os.environ


print (os.curdir)

print (os.getcwd())


# Access folder
os.listdir(r"C:\Users\Administrator\Desktop\study")

# create new folder
os.mkdir("sunck")

# view folder peoperties
os.stat("sunck")


# rename folder
os.rename("sunck", "lpc")


# delete folder
os.rmdir("lpc")

# delete file
#os.remove("ShareX_2018-09-23_13-08-25.png")

os.system("notepad")

os.system("write")

os.system("msconfig")

os.system("shutdown -s -t 500")

os.system("shutdown -a")

#os.system("taskkill /f /im notepad.exe")

# function of os moudle

print(os.path.abspath("./sunck"))

# Stitching path,  Versatility
p1 = r"C:\Users\Administrator\Desktop\study\python学习"
p2 = r"python全栈学习"
p3 = os.path.join(p1, p2)

# split path
p4 = os.path.split(p1)

p5 = os.path.splitext(p1)


# judge if it is a dir
p6 = os.path.isdir(p1)

# judge if it is presence
p7 = os.path.isfile(p1)

# judge if a dir presence
p8 = os.path.exists(p1)


# get the large of a file
p9 = os.path.getsize(p1)

# get the dir of a file
p10 = os.path.normcase(p1)


# windows control display and hide
"""
# find the id of a process
QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")

# hide window
win32gui.ShowWindow(QQWin, win32con.SW_HIDE)

win32gui.ShowWindow(QQWin, win32con.SW_SHOW)
# hide show window
"""
while True:
    QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")
    win32gui.ShowWindow(QQWin, win32con.SW_HIDE)
    time.sleep(2)
    win32gui.ShowWindow(QQWin, win32con.SW_SHOW)
    time.sleep(2)
"""

# para1: the window you want control
# para1: nearly location HWND_TOPMOST
# para1: x
# para1: y
# para2: l
# para1: w
# x = 100
# while True:
win32gui.SetWindowPos(QQWin,win32con.HWND_TOP,100,200,300,400,win32con.SWP_SHOWWINDOW)
# x = x+10
# time.sleep(1)


# speaker = win32com.client.Dispath("sio")

PROCESS_ALL_ACCESS = (0x000F0000|0x00100000|0xFFF)

# find window

QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")

# find pid
hid, pid = win32process.GetWindowThreadProcessId(QQWin)

# open process with highest level
p = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, pid)


# data = ctypes.c_long()
# load stroge moudle


