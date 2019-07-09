#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/7/24 10:44
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : lucky_dice.py
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
from com.android.monkeyrunner import MonkeyRunner, MonkeyImage, MonkeyDevice


def launch_app():
    device = MonkeyRunner.waitForConnection(3)

    device.startActivity(component='com.x1.ui/.SplashActivity')

    print("启动应用成功")

    return device


def get_into_cat_paradise(device):
    # 触摸操作，三个参数，X坐标，Y坐标，触摸类型
    device.touch(150, 1832, 'DOWN_AND_UP')
    print("点击'首页'")

    MonkeyRunner.sleep(10)
    device.touch(745, 1832, 'downAndUp')
    print("点击'我的'成功")

    MonkeyRunner.sleep(1)
    device.touch(533, 1544, 'downAndUp')
    print("进入'猫乐园'")


def get_into_lucky_dice(device):
    MonkeyRunner.sleep(1)
    device.touch(806, 688, 'downAndUp')
    print("点击掷骰子")

    MonkeyRunner.sleep(5.0)
    # 移动操作，四个参数，起始位置坐标，结束位置坐标，持续时间，步数
    device.drag((432, 1536), (432, 307), 0.1, 1)
    print("划到最底下")

    MonkeyRunner.sleep(0.5)
    device.touch(533, 1760, 'downAndUp')
    print("点击开始")

    MonkeyRunner.sleep(0.5)
    device.touch(378, 1064, 'downAndUp')
    print("确认消耗猫粮")

    MonkeyRunner.sleep(5.0)
    device.touch(533, 1272, 'downAndUp')
    print("确认获得猫粮")


if __name__ == '__main__':
    device = launch_app()

    get_into_cat_paradise(device)

    get_into_lucky_dice(device)
