# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyprojectPipeline(object):
    def process_item(self, item, spider):
        return item


class PojPipeline(object):
    def process_item(self, item, spider):
        if item['result'] != 'Accepted':
            item['time'] = '-1MS'
            item['memory'] = '-1K'
        return item
