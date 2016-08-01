# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 书名
    name = scrapy.Field()

    # 作者
    author = scrapy.Field()

    # 书信息
    bookinfo = scrapy.Field()

    # 一星百分数
    onestar = scrapy.Field()

    # 二星百分数
    twostar = scrapy.Field()

    # 三星百分数
    threestar = scrapy.Field()

    # 四星百分数
    fourstar = scrapy.Field()

    # 五星百分数
    fivestar = scrapy.Field()

    # 豆瓣评分
    score = scrapy.Field()

    # 评论数
    commentNum = scrapy.Field()





    # 出版年
    #year = scrapy.Field()

    # 出版社
    #publisher = scrapy.Field()

    # 页数
    #pageNum = scrapy.Field()

    # 价格
    #price = scrapy.Field()

