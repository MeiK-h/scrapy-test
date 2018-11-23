# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PojSubmission(scrapy.Item):
    run_id = scrapy.Field()
    user = scrapy.Field()
    problem = scrapy.Field()
    result = scrapy.Field()
    memory = scrapy.Field()
    time = scrapy.Field()
    language = scrapy.Field()
    code_length = scrapy.Field()
    submit_time = scrapy.Field()
