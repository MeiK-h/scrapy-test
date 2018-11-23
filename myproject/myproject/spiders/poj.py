# -*- coding: utf-8 -*-
import scrapy

from myproject.items import PojSubmission


class PojSpider(scrapy.Spider):
    name = 'poj'
    allowed_domains = ['poj.org']

    def start_requests(self):
        self.username = getattr(self, 'username', 'dhu_try')
        yield scrapy.Request(url='http://poj.org/status?user_id={username}&bottom=0'.format(username=self.username))

    def parse(self, response):
        first_line_flag = True
        for trs in response.css('tr[align="center"]'):
            tds = trs.css('td::text').extract()
            srcs = trs.css('a::text').extract()
            font = trs.css('font::text').extract()
            if font[0] != 'Accepted':
                tds.insert(1, '0MS')
                tds.insert(1, '0K')

            submission = PojSubmission()
            submission['run_id'] = tds[0]
            submission['user'] = srcs[0]
            submission['problem'] = srcs[1]
            submission['result'] = font[0]
            submission['memory'] = tds[1]
            submission['time'] = tds[2]
            submission['language'] = tds[3]
            submission['code_length'] = tds[4]
            submission['submit_time'] = tds[5]

            yield submission

            if first_line_flag:
                yield scrapy.Request(url='http://poj.org/status?user_id={username}&bottom={bottom}'.format(username=self.username, bottom=tds[0]))
                first_line_flag = False
