# -*- coding: utf-8 -*-

import scrapy


class PiItem(scrapy.Item):
    url = scrapy.Field()
    code = scrapy.Field()
    address = scrapy.Field()
    beds = scrapy.Field()
    baths = scrapy.Field()
    area_total = scrapy.Field()
    area_util = scrapy.Field()
    clp = scrapy.Field()
    uf = scrapy.Field()
    date = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
