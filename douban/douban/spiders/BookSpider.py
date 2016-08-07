#!/usr/bin/env python
# coding=utf-8

import numpy as np

import scrapy
from scrapy.selector import Selector
from douban.items import BookItem

class BookSpider(scrapy.Spider):
    name = "book.douban"
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/']

    # 抽取标签页面的所有Tag链接，生成对应的请求
    def parse(self, response):
	links = response.xpath("//*[@class = 'tagCol']/descendant::a/@href").extract()
        for href in links:
            for pageNum in np.linspace(0, 180, 10): # 抓取每个Tag的前10页书籍
                full_url = response.urljoin(href + "/?start=" + str(int(pageNum)) + "&type=S") # ?type=S  目的是按评价排序
                yield scrapy.Request(full_url, callback=self.parse_tag_per_page)

    # 抽取对应标签页面的所有书籍链接
    def parse_tag_per_page(self, response):
	links = response.xpath("//ul[@class = 'subject-list']/descendant::a[@class = 'nbg']/@href").extract()
        for book in links:
            yield scrapy.Request(book, callback=self.parse_book)

    # 抽取每本书籍，并将其存入对应的BookItem
    def parse_book(self, response):
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

