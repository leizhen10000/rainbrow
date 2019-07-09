#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/3 17:29
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : config_util.py
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
import os
from configparser import ConfigParser

import yaml


class ConfigSelector():
    pass


def get_conf():
    f = open('hwy_config.yaml')
    x = yaml.load(f)
    print(x)


if __name__ == '__main__':
    get_conf()
