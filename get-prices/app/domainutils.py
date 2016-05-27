# -*- coding: utf-8 -*-
import re

DOMAIN_JD = "jd"
DOMAIN_TMALL = "tmall"

REG_JD = ".*item.jd.com.*"


def get_domain(url):
    m = re.match(REG_JD, url)
    if m:
        return DOMAIN_JD
    return None
