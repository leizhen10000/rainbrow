#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2019-06-16 15:37
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : handle.py
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
import hashlib
import traceback

import web

from wechat import receive, reply

urls = (
    '/wx', 'Handle'
)


class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "helloking123aw3412"  # 请按照公众平台官网\基本配置中信息填写

            list1 = [token, timestamp, nonce]
            list1.sort()
            tmp = ''.join(list1)
            sha1 = hashlib.sha1(tmp.encode('utf-8'))
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as e:
            print(e)
            return

    def POST(self):
        try:
            web_data = web.data()
            print("Handle/Post web data is\n", str(web_data))
            rec_msg = receive.parse_xml(web_data)
            if isinstance(rec_msg, receive.Msg) and rec_msg.msg_type == 'text':
                to_user = rec_msg.from_user_name
                from_user = rec_msg.to_user_name
                content = rec_msg.content
                reply_msg = reply.TextMsg(to_user, from_user, content)
                return reply_msg.send()
        except Exception as e:
            print("出现异常", e)
            print(traceback.print_exc())


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
