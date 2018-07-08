# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from douban.items import DoubanItem


class DbmovieSpider(CrawlSpider):
    '''使用Rule提出每一页链接, 以及详情页链接'''
    name = 'dbmovie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    rules = (
        Rule(LinkExtractor(allow=r'start=(\d+)&filter='), follow=True),
        Rule(LinkExtractor(allow=r'subject/(\d+)'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        '''从从详情页响应文件中提出需要的信息, 放入管道中待处理'''
        item = DoubanItem()

        item['number'] = response.xpath('//div[@class="top250"]/span[@class="top250-no"]/text()').extract()[0].split('.')[-1]
        item['movie'] = response.xpath('//h1/span[@property="v:itemreviewed"]/text()').extract()[0].split(' ')[0]
        item['score'] = response.xpath('//div[@id="interest_sectl"]//strong/text()').extract()[0]
        item['director'] = response.xpath('//div[@id="info"]//a[@rel="v:directedBy"]/text()').extract()[0]
        item['star'] = ', '.join(response.xpath('//div[@id="info"]//span[@class="actor"]//a[@rel="v:starring"]/text()').extract())
        text = response.xpath('//div[@class="related-info"]//span[@property="v:summary"]/text()').extract()
        content = []
        for i in text:
            content.append(i.strip())
        item['content'] = ''.join(content)

        yield item
