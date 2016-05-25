# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.item import Item,Field

from myscrapy.dbutils import query_item
import scrapy
import json

class JdItem(scrapy.Item):
    title = Field()
    price = Field()
    pass

def test_db_utils():
    items = query_item()
    for item in items:
        print 'link:' + item.link
        print 'title:' + item.title

class JdSpider(BaseSpider):
    name = "jd"
    allowed_domains = ["jd.com","p.3.cn"]
    item_url = "http://item.jd.com/2329029.html"
    start_urls = [
            item_url,
    ]
    PRICE_URL_PREFIX = "http://p.3.cn/prices/get?type=1&area=1_72_4137&pdtk=&pduid=786038329&pdpin=&pdbp=0&callback=cnp&skuid=J_"
    def getUrls(self):
        pass


    def parse(self, response):
        test_db_utils()
        #hxs = HtmlXPathSelector(response)
        lst = response.url.split('/')
        item_id =  lst[-1].split('.')[0]
        #print response.body
        #price = response.selector.xpath('//strong[@id="jd-price"]/text()').extract()
        price_url = self.PRICE_URL_PREFIX + item_id
        request = scrapy.Request(price_url, callback=self.parse_price)
        price = ""
        title = response.selector.xpath('//div[@id="name"]/h1/text()').extract()
        item = JdItem()
        item['title'] = title[0]
        request.meta['item'] = item
        return request
    def parse_price(self, response):
        item = response.meta['item']
        result = response.body
        part_a = result.split('[')[1]
        part_b = part_a.split(']')[0]
        data = json.loads(part_b)
        if 'p' in data:
            item['price'] = data['p']
        return item
