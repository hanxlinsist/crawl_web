# -*- coding: utf-8 -*-

from functools import wraps

def check_spider_pipeline(process_item_method):

    @wraps(process_item_method)
    def wrapper(self, item, spider):

        # if class is in the spider's pipeline, then use the
        # process_item method normally.
        if self.__class__ in spider.pipeline:
            return process_item_method(self, item, spider)

        # otherwise, just return the untouched item (skip this step in the pipeline)
        else:
            return item

    return wrapper
