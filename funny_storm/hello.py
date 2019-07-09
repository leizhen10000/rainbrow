#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019-07-01 09:53
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : hello.py
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
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


print(__name__)
