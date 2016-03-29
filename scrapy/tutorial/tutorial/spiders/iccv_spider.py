from scrapy.spider import BaseSpider
from scrapy.selector import Selector





class ICCVSpider(BaseSpider):
    name='iccv'
    allowed_domains=['http://www.cv-foundation.org/']
    start_urls = [
            'http://www.cv-foundation.org/openaccess/content_iccv_2015/papers/'
            ]

    def parse(self,response):
        #print response.body
        links = response.selector.xpath('//@href')
        for link in links:
            print link.extract()


