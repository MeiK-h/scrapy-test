# -*- coding: utf-8 -*-
import scrapy


class Rating(scrapy.Item):
    username = scrapy.Field()
    country = scrapy.Field()
    rating = scrapy.Field()
