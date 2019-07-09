#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019-07-04 16:50
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : new_main_asdfa.py
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
import logging

from common.log_more import setup_logging


setup_logging()
logger = logging.getLogger("qop")
logger.info("bbbb")
logger.error('there is an error .')
# logger.error("aabasd")
# logger.info('darea')
