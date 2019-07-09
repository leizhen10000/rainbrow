#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2019-06-20 10:20
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : reply.py
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
import re
import time
import traceback

import pymysql

from wechat.new_email import send_mail


class Msg:
    def __init__(self):
        pass

    def send(self):
        return "success"


class TextMsg(Msg):
    def __init__(self, to_user_name, from_user_name, content):
        super().__init__()
        self.__dict = dict()
        self.__dict['ToUserName'] = to_user_name
        self.__dict['FromUserName'] = from_user_name
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self):
        text_content = self.__dict['Content']
        if re.match(r'\d{6}', text_content):
            print("当前股票为", text_content)
            result = _query_ticket_detail(str(text_content))
            if result.get('message'):
                self.__dict['Content'] = result['message']
            else:
                self.__dict['Content'] = self._build2(result)
        else:
            self.__dict['Content'] = 'welcome!'
        xml_form = """
                <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[{Content}]]></Content>
                </xml>
                """
        return xml_form.format(**self.__dict)

    def _build2(self, result: dict) -> str:
        """构建返回信息二

        模版：
        股票供给与需求：前3个月解禁a股，占解禁前的流通股数的b%；未来3个月将要解禁b股，
        占目前流通股数的c%. 昨日成交金额a亿，全A排名100/3500；昨日换手率4，全A排名
        100/3500；昨日融资买入比例5，全A排名4/1000
        """
        result = {key: value if value is not None else 0 for key, value in result.items()}
        # 前3个月解禁n股,n为解禁数量,number_3_month_before
        n3mb = result['threemonthsbeforliftamount']
        # 前3个月解禁占流通股比，rate_of_number_3_month_before
        rn3mb = result['threemonthsbeforliftaratio']
        # 后3个月解禁n股,n为解禁数量,number_3_month_after
        n3ma = result['threemonthafterliftamount']
        # 后3个月解禁占流通股比，rate_of_number_3_month_after
        rn3ma = result['threemonthafterliftratio']
        # 成交金额 单位亿，turnoverValue
        tov = result['turnoverValue']
        # 成交金额全A排名,turnoverValuerank
        tovr = result['valueRank']  # 这里不是取原职
        # 换手率 单位亿，turnoverRate
        tor = result['turnoverRate']
        # 换手率全A排名,turnoverRaterank
        torr = result['rateRank']  # 这里不是取原职
        # 当日融资买入比例, finBuyValratio
        fbvr = result['finBuyValratio']
        # 当日融资买入比例排名, finBuyValratiorank
        fbvrr = result['ratioRank']  # 这里不是取数据库原值

        return f"股票供给与需求：前3个月解禁{n3mb}股，占解禁前的流通股数的{rn3mb}%；未来3个月将要解禁{n3ma}股，占目前流通股数的{rn3ma}%. 昨日成交金额{tov}亿，全A排名{tovr}；昨日换手率{tor}，全A排名{torr}；昨日融资买入比例{fbvr}，全A排名{fbvrr}"


def _query_ticket_detail(ticker: str) -> dict:
    """根据股票代码查询结果

    @:param ticker 股票代码
    """
    connect = pymysql.Connect('49.234.41.17', 'quant', 'X3Q5PQPkZjsm', 'quantdw', 3317,
                              charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try:
        with connect.cursor() as cursor:
            sql = ("SELECT threemonthsbeforliftamount,"
                   "threemonthsbeforliftaratio,"
                   "threemonthafterliftamount,"
                   "threemonthafterliftratio,"
                   "CONCAT(ROUND(turnoverRate * 100, 2), '%')   turnoverRate,"
                   "CONCAT(turnoverRaterank, '/', s1.count)     rateRank,"
                   "ROUND(turnoverValue / 100000000, 2)         turnoverValue,"
                   "CONCAT(turnoverValuerank, '/', s1.count)    valueRank,"
                   "CONCAT(ROUND(finBuyValratio * 100, 2), '%') finBuyValratio,"
                   "CONCAT(finBuyValratiorank, '/', s1.count)   ratioRank "
                   "FROM quantdw.Stock,"
                   "  (SELECT COUNT(*) count"
                   "   FROM quantdw.Stock) s1 "
                   "LIMIT 1")
            cursor.execute(sql)
            result = cursor.fetchall()
            if (not result) or (len(result) < 1):
                print("当前%s查询无结果，请检查".format(ticker))
                return {"message": "welcome，您输入的股票代码有误，请输入正确的内容如：000002"}
            elif len(result) != 1:
                send_mail(f"查询的股票{ticker}结果超过一条，请查看")
            else:
                print("查询结果为", result[0])
            connect.commit()
        return result[0]
    except Exception as e:
        send_mail('查询的股票{ticker}\n异常：\n\t' + str(e))
        traceback.print_exc()
    finally:
        connect.close()


class ImageMsg(Msg):
    def __init__(self, to_user_name, from_user_name, media_id):
        Msg.__init__()
        self.__dict = dict()
        self.__dict['ToUserName'] = to_user_name
        self.__dict['FromUserName'] = from_user_name
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = media_id

    def send(self):
        xml_form = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        </Image>
        </xml>
        """

        return xml_form.format(**self.__dict)
