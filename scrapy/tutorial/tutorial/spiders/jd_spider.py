# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import Selector

from tutorial.items import JdItem

class JdSpider(BaseSpider):
    name = "jd"
    allowed_domains = ["jd.com"]
    start_urls = [
            "http://item.jd.com/2329029.html"
    ]

    def parse(self, response):
        #hxs = HtmlXPathSelector(response)
        print response.body
        price = response.selector.xpath('//strong[@id="jd-price"]/text()').extract()
        title = response.selector.xpath('//div[@id="name"]/h1/text()').extract()
        print title[0].encode('utf-8')
        item = JdItem()
        item['price'] = price
        item['title'] = title
        return item

