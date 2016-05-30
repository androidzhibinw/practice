# -*- coding: utf-8 -*-
import re

DOMAIN_JD = "jd"
DOMAIN_TMALL = "tmall"
DOMAIN_AMAZON = "amazon"

REG_JD = ".*item.jd.com.*"
REG_AMAZON = ".*www.amazon.cn.*"


def get_domain(url):
    m = re.match(REG_JD, url)
    if m:
        return DOMAIN_JD
    m = re.match(REG_AMAZON,url)
    if m:
        return DOMAIN_AMAZON
    return None
