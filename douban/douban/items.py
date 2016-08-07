# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):

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

    # 标签
    tag = scrapy.Field()

    # 最热门短评
    review = scrapy.Field()

    # 最热门短评时间
    reviewTime = scrapy.Field()

    # 最热门短评人网名
    reviewName = scrapy.Field()

    # 最热门短评人ID. 比如：https://www.douban.com/people/85234374/   ID为85234374
    ID = scrapy.Field()

    # 短评的有用数
    reviewHelpfulNum = scrapy.Field()

