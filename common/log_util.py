#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019-07-03 17:54
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : log_util.py
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
import os
import sys
from os.path import abspath, dirname, join

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger('test')

# StreamHandler
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(level=logging.DEBUG)
logger.addHandler(stream_handler)

file_path = abspath(join(dirname(__file__)))
log_file = join(file_path, os.path.pardir, 'resource/output.log')
# FileHandler
file_handler = logging.FileHandler(log_file, encoding='utf-8')
file_handler.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s [ %(name)s ] %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Log
logger.info('This is a log info')
logger.debug('Deb')
logger.warning('Warning exists')
