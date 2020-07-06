# -*- coding: utf-8 -*-
import scrapy


class PlayersSpider(scrapy.Spider):
    name = 'scoring'
    allowed_domains = ['www.pgatour.com']
    start_urls = ['https://www.pgatour.com/stats/categories.RSCR_INQ.html']

    def parse(self, response):
        scr = response.xpath("//li[@data-category-index]")
        for link in scr:
            yield{
                'name': link.xpath(".//a/text()").get(),
                'link': link.xpath(".//a/@href").get()
            }
