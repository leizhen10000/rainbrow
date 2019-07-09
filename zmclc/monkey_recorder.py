#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/7/24 10:41
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : monkey_recorder.py
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
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner.recorder import MonkeyRecorder as recorder

# 连接设备，启动录制器
device = mr.waitForConnection(3)
recorder.start(device)


