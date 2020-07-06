# -*- coding: utf-8 -*-
import scrapy


class PlayersSpider(scrapy.Spider):
    name = 'streaks'
    allowed_domains = ['www.pgatour.com']
    start_urls = ['https://www.pgatour.com/stats/categories.RSTR_INQ.html']

    def parse(self, response):
        streak = response.xpath("//li[@data-category-index]")
        for link in streak:
            yield{
                'name': link.xpath(".//a/text()").get(),
                'link': link.xpath(".//a/@href").get()
            }
