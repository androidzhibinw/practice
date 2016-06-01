 # -*- coding: utf-8 -*-
import requests
import re
import json
from scrapy.selector import Selector
from app.dbutils import update_item_title,query_item,save_price
from app.domainutils import DOMAIN_JD, DOMAIN_AMAZON,DOMAIN_KAOLA
from app import app

PRICE_URL_PREFIX = "http://p.3.cn/prices/get?type=1&area=1_72_4137&pdtk=&pduid=786038329&pdpin=&pdbp=0&callback=cnp&skuid=J_"

def get_http_response(url):
    return requests.get(url).text

def get_jd_price_url(item_url):
    app.logger.info('get_jd_price_url:' +item_url)
    lst = item_url.split('/')
    item_id =  lst[-1].split('.')[0]
    return PRICE_URL_PREFIX+item_id
def scrapy():
    items = query_item()
    for item in items:
        fetch_one(item)
 
def fetch_one(item):
    print item.domain
    if item.domain == DOMAIN_JD:
        fetch_one_jd(item)
    elif item.domain == DOMAIN_AMAZON:
        fetch_one_amazon(item)
    elif item.domain == DOMAIN_KAOLA:
        fetch_one_kaola(item)
    else:
        app.logger.info("domain not supported")

def fetch_one_kaola(item):
    item_url = item.link
    txt = get_http_response(item_url)
    if item.title is None :
        title = parse_kaola_title(txt)
        if title:
            update_item_title(item.link,title)
    price = parse_kaola_price(txt)
    if price:
        f_price = float(price)
        save_price(item.link,f_price)

def parse_kaola_title(txt):
    title = Selector(text=txt).xpath('//div[@class="crumbs"]/span/text()').extract()
    if title:
        app.logger.info('kaola title:' + title[0])
        return title[0]
    else:
        app.logger.error('kaola get title fail!')
    return None
def parse_kaola_price(txt):
    price = Selector(text=txt).xpath('//span[@id="js_currentPrice"]/span/text()').extract()
    if price:
        app.logger.info('kaola price:' + price[0])
        return price[0]
    else:
        app.logger.info('kaola price not get!')
    return None

def fetch_one_jd(item):
    item_url = item.link
    #title
    if item.title is None:
        r = requests.get(item_url)
        title = Selector(text=r.text).xpath('//div[@id="name"]/h1/text()').extract()
        if title:
            update_item_title(item.link,title[0])
        else:
            app.logger.info('fail to get title')

    price_url = get_jd_price_url(item_url)
    price_reponse = requests.get(price_url)
    price = parse_price_jd(price_reponse.text)
    if price:
        f_price = float(price)
        save_price(item.link,f_price)

def parse_price_jd(text):
    part_a = text.split('[')[1]
    part_b = part_a.split(']')[0]
    data = json.loads(part_b)
    if 'p' in data:
        price = data['p']
        return price
    else:
        return None

def fetch_one_amazon(item):
    item_url = item.link
    r = requests.get(item_url)
if __name__ == '__main__':
    scrapy()
