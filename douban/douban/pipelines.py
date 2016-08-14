# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import re
from MyTools import check_spider_pipeline

class BookInfoPipeline(object):

    @check_spider_pipeline
    def process_item(self, item, spider):
        str = ""
        for e in item["bookinfo"]:
            if re.search(r'^\s*$', e):
                print "drop this element"
            else:
                str = str + e + ","
	item["bookinfo"] = str[:-1]

        if item['name']:
            if item['author']:
                return item
            else:
                raise DropItem("Missing name or author in %s" % item)


class IDPipeline(object):

    @check_spider_pipeline
    def process_item(self, item, spider):
	id_str = ''.join(item["ID"]) # 把列表中的要元素合并成一个字符串
	url_list = filter(len, id_str.split('/')) # 过滤列表中的空串
	item["ID"] = url_list[len(url_list) - 1] # 提取ID

	return item
