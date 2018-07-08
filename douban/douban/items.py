# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # 排名
    number = scrapy.Field()
    # 电影名
    movie = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 导演
    director = scrapy.Field()
    # 主演
    star = scrapy.Field()
    # 简介
    content = scrapy.Field()