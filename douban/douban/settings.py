# -*- coding: utf-8 -*-

# Scrapy settings for douban project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'douban'

# Scrapy寻找spiders的地方，这是一个列表结构，你可以指定多个地方。
SPIDER_MODULES = ['douban.spiders']

# 用scrapy genspider [-t template] <name> <domain>命令生成的spider所放的地方
NEWSPIDER_MODULE = 'douban.spiders'

# Retry many times since proxies often fail
RETRY_TIMES = 10
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

# 如果你不想用代理IP去抓取网页，注释掉下面的前三个组件。第四个组件的目的是定制自己request header.
DOWNLOADER_MIDDLEWARES = {
#	'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
#	'douban.randomproxy.RandomProxy': 100,
#	'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
	'douban.MyMiddlewares.CustomUserAgentMiddleware':345,
}

# 把这个路徑改成你自己
PROXY_LIST = '/home/vincent/crawl_web/douban/proxy_list.txt'

# Configure item pipelines
ITEM_PIPELINES = {
    'douban.pipelines.BookInfoPipeline': 300,
    'douban.pipelines.IDPipeline': 500,
}




DOWNLOAD_DELAY = 2
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=False
# The initial download delay
#AUTOTHROTTLE_START_DELAY=3
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=12
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False
