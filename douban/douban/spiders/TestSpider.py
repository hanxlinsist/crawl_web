#!/usr/bin/env python
# coding=utf-8

import numpy as np

import scrapy
from scrapy.selector import Selector
from douban.items import BookItem
from douban.pipelines import IDPipeline

class TestSpider(scrapy.Spider):
    name = "douban.test"
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/subject/6082808/']

    pipeline = set([
       IDPipeline,
    ])

    # 抽取每本书籍，并将其存入对应的BookItem
    def parse(self, response):
        item = BookItem()
        sel = Selector(response)
        e = sel.xpath("//div[@id='wrapper']")
        item['name'] = e.xpath("./descendant::h1/descendant::span/text()").extract()
        item['author'] = e.xpath("//*[@id='info']/span[1]/a/text()").extract()
        item['bookinfo'] = e.xpath("//*[@id='info']/text()").extract()
        item['score'] = e.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()').extract()
        item['commentNum'] = e.xpath('//*[@id="interest_sectl"]/descendant::span[@property = "v:votes"]/text()').extract()

        item['fivestar'] = e.xpath('//*[@id="interest_sectl"]/descendant::span[@class = "rating_per"][1]/text()').extract()
        item['fourstar'] = e.xpath('//*[@id="interest_sectl"]/descendant::span[@class = "rating_per"][2]/text()').extract()
        item['threestar'] = e.xpath('//*[@id="interest_sectl"]/descendant::span[@class = "rating_per"][3]/text()').extract()
        item['twostar'] = e.xpath('//*[@id="interest_sectl"]/descendant::span[@class = "rating_per"][4]/text()').extract()
        item['onestar'] = e.xpath('//*[@id="interest_sectl"]/descendant::span[@class = "rating_per"][5]/text()').extract()

        item['tag'] = response.xpath("//*[@id = 'db-tags-section']/descendant::a/text()").extract()

        request = scrapy.Request(response.url + "/comments/hot", callback=self.parse_review) # 发送书籍对应的短评请求
        request.meta['item'] = item

        return request


    # 抽取书籍的热门短评信息
    def parse_review(self, response):
        item = response.meta['item']

        item['review'] = response.xpath("//*[@id = 'comment-list-wrapper']/descendant::li[@class = 'comment-item'][1]/p/text()").extract()

        item['reviewTime'] = response.xpath("//*[@id = 'comment-list-wrapper']/descendant::li[@class = 'comment-item'][1]/descendant::span[@class='comment-info']/span[last()]/text()").extract()

        item['reviewName'] = response.xpath("//*[@id = 'comment-list-wrapper']/descendant::li[@class = 'comment-item'][1]/descendant::span[@class='comment-info']/a/text()").extract()

        item['ID'] = response.xpath("//*[@id = 'comment-list-wrapper']/descendant::li[@class = 'comment-item'][1]/descendant::span[@class='comment-info']/a/@href").extract()

        item['reviewHelpfulNum'] = response.xpath("//*[@id = 'comment-list-wrapper']/descendant::li[@class = 'comment-item'][1]/descendant::span[@class='comment-vote']/span/text()").extract()

        return item

