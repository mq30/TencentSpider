# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentInfo(scrapy.Item):
    # 职位名称
    positionName = scrapy.Field()
    # 工作类型
    positionType = scrapy.Field()
    # 职位链接
    positionLink = scrapy.Field()
    # 人数
    positionPeople = scrapy.Field()
    # 工作地址
    workadd = scrapy.Field()
    # 发布时间
    releasstime = scrapy.Field()


class TencentContent(scrapy.Item):
    # 工作职责
    operatingduty = scrapy.Field()
    # 工作要求
    jobrequirements = scrapy.Field()
