# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from settings import USER_AGENT_LIST
import random
import base64


# 处理随即User-Agent
class RandomUserAgent(object):
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        # request.headers.setdefault("User-Agent", user_agent)
        request.headers["User-Agent"] = user_agent

# # 给请求设置代理,有个base64的认证
# class ProxyMiddleware(object):
#
#     def process_request(self, request, item):
#         proxy = "122.114.214.159:16816"
#         request.meta["proxy"] = "http://" + proxy
#
#         passwd = "mr_mao_hacker:sffqry9r"
#         b_passwd = base64.b16decode(passwd)
#         request.headers["Proxy-Authorization"] = "Basic " + b_passwd #  Basic 后边有个空格
