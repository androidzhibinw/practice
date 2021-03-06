# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import Selector

from tutorial.items import JdItem
import scrapy
import json

class JdSpider(BaseSpider):
    name = "jd"
    allowed_domains = ["jd.com","p.3.cn"]
    item_url = "http://item.jd.com/2329029.html"
    start_urls = [
            item_url,
            "http://item.jd.com/1514794.html"
    ]
    PRICE_URL_PREFIX = "http://p.3.cn/prices/get?type=1&area=1_72_4137&pdtk=&pduid=786038329&pdpin=&pdbp=0&callback=cnp&skuid=J_"

    def parse(self, response):
        #hxs = HtmlXPathSelector(response)
        lst = response.url.split('/')
        item_id =  lst[-1].split('.')[0]
        #print response.body
        #price = response.selector.xpath('//strong[@id="jd-price"]/text()').extract()
        price_url = self.PRICE_URL_PREFIX + item_id
        print price_url
        request = scrapy.Request(price_url, callback=self.parse_price)
        price = ""
        title = response.selector.xpath('//div[@id="name"]/h1/text()').extract()
        item = JdItem()
        item['title'] = title[0]
        print title[0].encode('utf-8')
        request.meta['item'] = item
        return request
    def parse_price(self, response):
        item = response.meta['item']
        result = response.body
        part_a = result.split('[')[1]
        print part_a
        part_b = part_a.split(']')[0]
        print part_b
        data = json.loads(part_b)
        if 'p' in data:
            item['price'] = data['p']
        print item
        return item
