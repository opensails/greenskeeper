# -*- coding: utf-8 -*-
import scrapy


class PlayersSpider(scrapy.Spider):
    name = 'approach'
    allowed_domains = ['www.pgatour.com']
    start_urls = ['https://www.pgatour.com/stats/categories.RAPP_INQ.html']

    def parse(self, response):
        app = response.xpath("//li[@data-category-index]")
        for link in app:
            yield{
                'name': link.xpath(".//a/text()").get(),
                'link': link.xpath(".//a/@href").get()
            }
