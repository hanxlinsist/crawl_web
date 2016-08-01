# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

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
        return item
