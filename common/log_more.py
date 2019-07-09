#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019-07-04 17:53
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : log_more.py
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
import logging.config
import os
import traceback
from datetime import datetime

import coloredlogs
import yaml

file_name = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir, 'resource/'))


def setup_logging(default_path=os.path.join(file_name, 'logging.yaml'),
                  default_level=logging.INFO, env_key='LOG_CFG'):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            try:
                config = yaml.safe_load(f.read())
                config = _rebuild_log_file_name(config)
                logging.config.dictConfig(config)
                # coloredlogs.install()
            except Exception as e:
                print(e)
                print("Error in Logging Configuration. Using default configs")
                traceback.print_exc()
                logging.basicConfig(level=default_level)
                # coloredlogs.install(level=default_level)
    else:
        logging.basicConfig(level=default_level)
        # coloredlogs.install(level=default_level)
        print("Failed to load configuration file. Using default configs")


def _rebuild_log_file_name(config):
    today = datetime.today()
    year, month = today.year, today.month
    dir_name = str(year) + "-" + str(month)
    for item in config['handlers']:
        handler = config['handlers'][item]
        if (handler['level'] in ['INFO', 'DEBUG']) and \
                (handler['class'] == 'logging.handlers.RotatingFileHandler'):
            log_file_name = handler['filename']
            names = log_file_name.split(r'/')
            log_dir_name = "/".join(names[:-1] + [dir_name])
            log_file_name = "/".join(names[:-1] + [dir_name] + names[-1:])
            if not os.path.exists(log_dir_name):
                os.makedirs(log_dir_name)
                print("生成文件")
            handler['filename'] = log_file_name
    return config
