# -*- coding: utf-8 -*-
import scrapy
import json
import pandas as pd

with open('C:/Users/Austin/Documents/PythonProjects/Golf/pga/all_links2.json', 'r') as agents:
    data = json.load(agents)
base = 'https://www.pgatour.com/'


class PlayersSpider(scrapy.Spider):
    name = 'collector'

    def start_requests(self):
        yield scrapy.Request(
            url='https://www.pgatour.com/stats',
            callback=self.parse,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
            }
        )

    def parse(self, response):
        for stat in data:
            yield scrapy.Request(url=base+stat['link'], callback=self.parse_stats, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
            })

    def parse_stats(self, response):
        category = response.xpath(
            ".//ul[@class='nav nav-tabs slim nav-tabs-drop']/li[@class='active']/a/text()").get()
        table_name = response.xpath(".//div[@class='header']//h1/text()").get()
        header_1 = response.xpath(
            "//table[@class='table-styled']//th[4]/text()").get()
        header_2 = response.xpath(
            "//table[@class='table-styled']//th[5]/text()").get()
        header_3 = response.xpath(
            "//table[@class='table-styled']//th[6]/text()").get()
        header_4 = response.xpath(
            "//table[@class='table-styled']//th[7]/text()").get()
        header_5 = response.xpath(
            "//table[@class='table-styled']//th[8]/text()").get()
        header_6 = response.xpath(
            "//table[@class='table-styled']//th[9]/text()").get()

        # Convert headers to strings

        header_1s = str(table_name) + '-' + str(header_1)
        if '.' in header_1s:
            header_1s = header_1s.replace('.', '')

        header_2s = str(table_name) + '-' + str(header_2)
        if '.' in header_2s:
            header_2s = header_2s.replace('.', '')

        header_3s = str(table_name) + '-' + str(header_3)
        if '.' in header_3s:
            header_3s = header_3s.replace('.', '')

        header_4s = str(table_name) + '-' + str(header_4)
        if '.' in header_4s:
            header_4s = header_4s.replace('.', '')

        header_5s = str(table_name) + '-' + str(header_5)
        if '.' in header_5s:
            header_5s = header_5s.replace('.', '')

        header_6s = str(table_name) + '-' + str(header_6)
        if '.' in header_6s:
            header_6s = header_6s.replace('.', '')

        table = response.xpath(".//table[@class='table-styled']//tbody/tr")
        for row in table:
            if not header_2:
                yield{
                    category + '-table_name': table_name,
                    'player': row.xpath(".//td[3]/a/text()").get(),
                    header_1s: row.xpath(".//td[4]/text()").get()
                }
            elif not header_3:
                yield{
                    category + '-table_name': table_name,
                    'player': row.xpath(".//td[3]/a/text()").get(),
                    header_1s: row.xpath(".//td[4]/text()").get(),
                    header_2s: row.xpath(".//td[5]/text()").get()
                }
            elif not header_4:
                yield{
                    category + '-table_name': table_name,
                    'player': row.xpath(".//td[3]/a/text()").get(),
                    header_1s: row.xpath(".//td[4]/text()").get(),
                    header_2s: row.xpath(".//td[5]/text()").get(),
                    header_3s: row.xpath(".//td[6]/text()").get()
                }
            elif not header_5:
                yield{
                    category + '-table_name': table_name,
                    'player': row.xpath(".//td[3]/a/text()").get(),
                    header_1s: row.xpath(".//td[4]/text()").get(),
                    header_2s: row.xpath(".//td[5]/text()").get(),
                    header_3s: row.xpath(".//td[6]/text()").get(),
                    header_4s: row.xpath(".//td[7]/text()").get()
                }
            elif not header_6:
                yield{
                    category + '-table_name': table_name,
                    'player': row.xpath(".//td[3]/a/text()").get(),
                    header_1s: row.xpath(".//td[4]/text()").get(),
                    header_2s: row.xpath(".//td[5]/text()").get(),
                    header_3s: row.xpath(".//td[6]/text()").get(),
                    header_4s: row.xpath(".//td[7]/text()").get(),
                    header_5s: row.xpath(".//td[8]/text()").get()
                }
            else:
                yield{
                    category + '-table_name': table_name,
                    'player': row.xpath(".//td[3]/a/text()").get(),
                    header_1s: row.xpath(".//td[4]/text()").get(),
                    header_2s: row.xpath(".//td[5]/text()").get(),
                    header_3s: row.xpath(".//td[6]/text()").get(),
                    header_4s: row.xpath(".//td[7]/text()").get(),
                    header_5s: row.xpath(".//td[8]/text()").get(),
                    header_6s: row.xpath(".//td[9]/text()").get()
                }
