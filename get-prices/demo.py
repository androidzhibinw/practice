from app.fetch import scrapy

from datetime import datetime
import time

ONE_HOUR = 60*60
if __name__ == '__main__':
    while True:
        dt = datetime.now()
        if dt.hour == 10:
            print 'doing scrapy at' + str(dt)
            scrapy()
        time.sleep(ONE_HOUR)



