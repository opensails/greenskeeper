# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo
import sqlite3


class MongodbPipeline(object):
    collection_name = "golfer_stats"

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(
            "mongodb+srv://Austin:Kummel91@golf-qegq1.mongodb.net/<dbname>?retryWrites=true&w=majority")
        self.db = self.client["PGA"]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)

        return item
# pass
# class SQLitePipeline(object):

#     def open_spider(self, spider):
#         self.collection = sqlite3.connect("pga.db")
#         self.c = self.collection.cursor()
#         self.c.execute('''
#             CREATE TABLE pga_stats(
#                 table_name TEXT,
#                 header_1 TEXT,
#                 header_2 TEXT,
#                 header_3 TEXT,
#                 header_4 TEXT,
#                 header_5 TEXT,
#                 header_6 TEXT,
#             )

#         ''')
#         self.connection.commit()

#     def close_spider(self, spider):
#         self.client.close()

#     def process_item(self, item, spider):
#         self.c.execute('''
#             INSERT INTO pga (tabel_name, header_1, header_2, header_3, header_4, header_5, header_6) VALUES(?,?,?,?,?,?,?)


#         ''', (
#             item.get('tabel_name'),
#             item.get('header_1'),
#             item.get('header_2'),
#             item.get('header_3'),
#             item.get('header_4'),
#             item.get('header_5'),
#             item.get('header_6'),
#         ))
#         self.connection.commit()

#         return item
