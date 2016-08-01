# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import re

class BookInfoPipeline(object):
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

