# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Tencent.items import TencentInfo
from Tencent.items import TencentContent


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0/']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'position_detail\.php\?id=\d+'), callback='parse_position', follow=False)
    )

    def parse_item(self, response):
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for node in node_list:
            item = TencentInfo()
            item['positionName'] = node.xpath("./td[1]/a/text()").extract()[0]
            item['positionLink'] = "http://hr.tencent.com/" + node.xpath("./td[1]/a/@href").extract()[0]
            try:
                item['positionType'] = node.xpath("./td[2]/text()").extract()[0]
            except:
                item['positionType'] = "NULL"
            item['positionPeople'] = node.xpath("./td[2]/text()").extract()[0]
            item['workadd'] = node.xpath("./td[2]/text()").extract()[0]
            item['releasstime'] = node.xpath("./td[2]/text()").extract()[0]

            yield item

    def parse_position(self, response):

        item = TencentContent()
        item['operatingduty'] = "".join(response.xpath("//ul[@class='squareli']")[0].xpath("./li/text()").extract())
        item['jobrequirements'] = "".join(response.xpath("//ul[@class='squareli']")[1].xpath("./li/text()").extract())

        yield item