# -*- coding: utf-8 -*-
import scrapy


class PlayersSpider(scrapy.Spider):
    name = 'pntrank'
    allowed_domains = ['www.pgatour.com']
    start_urls = ['https://www.pgatour.com/stats/categories.RPTS_INQ.html']

    def parse(self, response):
        pnt = response.xpath("//li[@data-category-index]")
        for link in pnt:
            yield{
                'name': link.xpath(".//a/text()").get(),
                'link': link.xpath(".//a/@href").get()
            }
