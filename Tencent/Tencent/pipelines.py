# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from Tencent.items import TencentInfo
from Tencent.items import TencentContent
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class TencentInfoPipeline(object):
    def __init__(self):
        self.f = open("tencentInfo.json", "w")

    def process_item(self, item, spider):
        if isinstance(item, TencentInfo):
            content = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.f.write(content)
        return item

    def close_item(self, spider):
        self.f.close()


class TencentContentPipeline(object):
    def __init__(self):
        self.f = open("tencentcont.json", "w")

    def process_item(self, item, spider):
        if isinstance(item, TencentContent):
            content = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.f.write(content)
        return item

    def close_item(self, spider):
        self.f.close()