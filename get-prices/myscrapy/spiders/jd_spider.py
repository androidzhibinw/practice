 # -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.item import Item,Field

import scrapy
import json

from myscrapy.dbutils import update_item_title,query_item,save_price

class JdItem(scrapy.Item):
    title = Field()
    price = Field()
    pass

def test_db_utils():
    items = query_item()
    for item in items:
        print item.link

class JdSpider(BaseSpider):
    name = "jd"
    allowed_domains = ["jd.com","p.3.cn"]
    start_urls = []
    oritinal_url=None
    items = query_item()
    for item in items:
        start_urls.append(item.link)
        print item.link
    PRICE_URL_PREFIX = "http://p.3.cn/prices/get?type=1&area=1_72_4137&pdtk=&pduid=786038329&pdpin=&pdbp=0&callback=cnp&skuid=J_"
    def getUrls(self):
        pass

    def parse(self, response):
        test_db_utils()
        #hxs = HtmlXPathSelector(response)
        self.oritinal_url = response.url
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
        update_item_title(response.url,title[0])
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
        f_price = float(item['price'])
        print f_price
        save_price(self.oritinal_url,f_price)
        return item
