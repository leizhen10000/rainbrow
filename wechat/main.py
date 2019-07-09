#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2019-06-16 16:10
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : main.py
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
import web
from .handle import Handle

urls = (
    '/wx', 'Handle'
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
