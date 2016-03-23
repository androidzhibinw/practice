import urllib,urllib2, os,json


course_url = 'http://www.jianki.com/api/courses'


def get_link_size(url):
    site = urllib.urlopen(url)
    meta = site.info()
    length = meta.getheaders('Content-Length')[0]
    print url+' size:',length
    return length


def get_links_size(link_list):
    amount = 0
    for link in link_list:
        amount+=get_link_size(link)
    return amount



##get json 
response = urllib2.urlopen(course_url).read()
data = json.loads(response)
result = data['result']
course = result[0]
days = course['days']
#print days
for day in days:
    actions = day['actions']
    amount = 0
    for action in actions:
        size=get_link_size(action['video_url'])
        print 'action',action['index'],'size:',size
        amount+=int(size)
    print 'day:',day['index'],',amount:',amount

#print get_link_size(url_1)
