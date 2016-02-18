# -*- coding: utf-8 -*-
import requests as rq
import json

MYAK ='Fduyk7ke8zCGBXFHu6W8u1KG'
MAP_URI = 'http://api.map.baidu.com/geocoder/v2/?output=json'
AK_PRE='&ak='
ADDR_PRE='&address='
ADDR='上海浦东新区金科路'
def get_position(address):
    lng=None
    lat=None
    success=False
    result = rq.get(MAP_URI + AK_PRE + MYAK + ADDR_PRE + address)
    json_result = json.loads(result.text)
    print json_result
    success = (json_result['status'] == 0)
    lat = json_result['result']['location']['lat']
    lng = json_result['result']['location']['lng']

    return success,lng,lat



print get_position(ADDR)

