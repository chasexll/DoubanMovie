# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings


class DoubanPipeline(object):
    '''将提出到的数据, 存入MongoDB数据库'''
    def __init__(self):
        '''
        初始化数据库连接
        '''
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DBNAME']
        sheet_name = settings['MONGODB_SHEET']

        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[db_name]
        self.mysheet = mydb[sheet_name]

    def process_item(self, item, spider):
        data = dict(item)
        self.mysheet.insert(data)
        return item
