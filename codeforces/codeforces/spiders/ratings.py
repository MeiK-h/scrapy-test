# -*- coding: utf-8 -*-
import scrapy

from codeforces.items import Rating


class RatingsSpider(scrapy.Spider):
    name = 'ratings'
    allowed_domains = ['codeforces.com']
    start_urls = ['http://codeforces.com/ratings/page/1']

    def parse(self, response):
        trs = response.css(
            '#pageContent > div.datatable.ratingsDatatable > div:nth-child(6) > table > tr')
        for tr in trs[1:]:
            rating = Rating()
            span = tr.css('a > span::text').extract_first()
            username = tr.css('a::text').extract_first()
            if span:
                username = span + username
            rating['username'] = username
            rating['country'] = tr.css('img::attr(alt)').extract_first()
            rating['rating'] = int(tr.css('td::text')[4].extract().strip())
            yield rating

        next_page = response.css('.arrow')
        for page in next_page:
            if page.css('::text').extract_first() == "\u2192":
                next_page_url = page.css('::attr(href)').extract_first()
                next_page_url = response.urljoin(next_page_url)
                yield scrapy.Request(url=next_page_url)
