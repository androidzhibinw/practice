# -*- coding: utf-8 -*-
import requests as rq
import json

MYAK ='Fduyk7ke8zCGBXFHu6W8u1KG'
MAP_URI = 'http://api.map.baidu.com/geocoder/v2/?output=json'
AK_PRE='&ak='
ADDR_PRE='&address='
LOCATION_PRE='&location='
POSI='&pois=1'
ADDR='上海浦东新区金科路'
addr ='上海黄浦区西藏中路268号来'
add2='翔殷路1003号'
add3=u'上海市徐汇区天钥桥路580号3楼'
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

def get_address(lng,lat):
    result = rq.get(MAP_URI+AK_PRE+MYAK+POSI+LOCATION_PRE+str(lat)+','+str(lng))
    print result.url
    json_result = json.loads(result.text.encode('utf-8'))
    return json_result


print get_position(add3)
print get_address(121.44861425015,31.191606250978)

