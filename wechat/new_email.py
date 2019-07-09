#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2019-06-27 11:26
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


def send_mail(message):
    try:
        server = smtplib.SMTP_SSL("smtp.exmail.qq.com", '465')
        server.login('mxy@hxyfavorite.top', "5oEY^dli!yJ0")
        server.sendmail('mxy@hxyfavorite.top', ['xingyuexinxi@163.com'], message)
        server.quit()
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件", e.args)
