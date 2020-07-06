# -*- coding: utf-8 -*-
import scrapy


class PlayersSpider(scrapy.Spider):
    name = 'around'
    allowed_domains = ['www.pgatour.com']
    start_urls = ['https://www.pgatour.com/stats/categories.RARG_INQ.html']

    def parse(self, response):
        arg = response.xpath("//li[@data-category-index]")
        for link in arg:
            yield{
                'name': link.xpath(".//a/text()").get(),
                'link': link.xpath(".//a/@href").get()
            }
