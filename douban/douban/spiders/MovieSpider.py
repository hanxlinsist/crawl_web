#!/usr/bin/env python
# coding=utf-8

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from douban.items import BookItem

class DoubanSpider(CrawlSpider):
    name = "douban"
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/']
    
    # A dictionary of settings that will be overridden from the project wide configuration when running this spider. 
    #It must be defined as a class attribute since the settings are updated before instantiation.
    custom_settings = {
        "DEPTH_LIMIT" : 3,
        "DOWNLOAD_TIMEOUT" : 190
        }


    rules = [
        Rule(LinkExtractor(allow=('/tag/互联网$', )), follow=True),
        Rule(LinkExtractor(allow=('\/subject\/\d+', )), callback='parse_item'),
    ]

    def parse_item(self, response):
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

        return item

