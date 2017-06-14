# -*- coding: utf-8 -*-
import scrapy

class InfPoiskItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()