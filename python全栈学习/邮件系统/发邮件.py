# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:38:04 2018

@author: LiPengcheng
"""
from email.mime.text import MIMEText
import smtplib

# smtp的服务器

SMTPSever = "smtp.163.com"

# 发邮件的地址
Sender = "gdgylpc@163.com"

# 发送者邮箱的密码
password = "123456789a"

# 先发送给服务器，服务器再发送给个人
message = "hello you "

# 将字符串转换为邮件文本
msg = MIMEText(message)

# 主题，即使标题
msg["Subject"] = "第一封Python发送的邮件"

# 发送者
msg["From"] = Sender

# 创建SMTP服务器
mailSever = smtplib.SMTP(SMTPSever, 25)

# 登录邮箱
mailSever.login(Sender, password)

# 发送邮件
mailSever.sendmail(Sender, ["gdgylpc@163.com", "1445895575@qq.com"], msg.as_string())

# 退出邮箱
mailSever.quit()
