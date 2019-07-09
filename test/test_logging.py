#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019-07-03 17:58
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : test_logging.py
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
from common.log_util import logger


def test_logger():
    logger.warning("Don't use this method")


def test_error():
    try:
        result = 10 / 0
    except Exception:
        logger.error('Failed to get result', exc_info=True)
    logger.info('Finish')


