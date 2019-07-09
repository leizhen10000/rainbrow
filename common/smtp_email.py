#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019-06-27 10:38
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : new_email.py
# @Software: PyCharm
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻┓
            ┃  ☃    ┃
            ┃ ┳┛  ┗┳ ┃
            ┃      ┻  ┃
            ┗━┓     ┏━┛
              ┃     ┗━━━┓
              ┃ 神兽保佑 ┣┓
              ┃ 永无BUG┏┛
              ┗┓┓┏━┳┓┏┛
               ┃┫┫ ┃┫┫
               ┗┻┛ ┗┻┛
"""
import smtplib
from email.header import Header
from email.mime.text import MIMEText

sender = 'mxy@hxyfavorite.top'
receivers = ['xingyuexinxi@163.com']

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header('微信公众号-挖矿文森特', 'utf-8')
message['To'] = Header('开发人员-疯狂的原子', 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 第三方 SMTP 服务
mail_host = "smtp.exmail.qq.com"
mail_user = sender
mail_pass = "5oEY^dli!yJ0"

try:
    server = smtplib.SMTP_SSL(mail_host, '465')
    server.login(mail_user, mail_pass)
    server.sendmail(sender, receivers, message)
    server.quit()
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件")
