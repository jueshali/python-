"""
Created on Mon Nov 12 21:38:04 2018

@author: Administrator
"""
import os


def work(path):
    with open(path, 'r') as f:
        while True:
            # laphae11985@163.com--198587
            line_info = f.readline()
            mail_str = line_info.split("--")[0]
            file_type = mail_str.split("@")[1].split(".")[1]
            dir_str = os.path.join(path,file_type)
            if not os._exists(dir_str):
                os.makedirs(dir_str)
            # creat file
            file_path = os.path.join(dir_str, file_type+".txt" + "a")
            with open(file_path, "a") as fw:
                fw.write(mail_str + "\n")


def get_file2(path):
    list2 = list()
    list3 = list()
    list2.append(path)
    while list2:
        temp = list2.pop()
        filelist = os.listdir(temp)
        for filename in filelist:
            temp1 = os.path.join(temp, filename)
            if os.path.isdir(temp1):
                list2.append(temp1)
            else:
                list3.append(temp1)
    return list3





























