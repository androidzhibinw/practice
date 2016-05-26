 # -*- coding: utf-8 -*-
import requests
import re
import json
from scrapy.selector import Selector
from app.dbutils import update_item_title,query_item,save_price

PRICE_URL_PREFIX = "http://p.3.cn/prices/get?type=1&area=1_72_4137&pdtk=&pduid=786038329&pdpin=&pdbp=0&callback=cnp&skuid=J_"


def get_jd_price_url(item_url):
    lst = item_url.split('/')
    item_id =  lst[-1].split('.')[0]
    return PRICE_URL_PREFIX+item_id
def scrapy():
    items = query_item()
    for item in items:
        fetch_one(item)
 
def fetch_one(item):
    fetch_one_jd(item)

def fetch_one_jd(item):
    item_url = item.link
    #title
    if item.title is None:
        r = requests.get(item_url)
        title = Selector(text=r.text).xpath('//div[@id="name"]/h1/text()').extract()
        update_item_title(item.link,title[0])

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


scrapy()
