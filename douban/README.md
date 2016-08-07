# spiders运行原理

1. You start by generating the initial Requests to crawl the first URLs, and specify a callback function to be called with the response downloaded from those requests.The first requests to perform are obtained by calling the start_requests() method which (by default) generates Request for the URLs specified in the start_urls and the parse method as callback function for the Requests.
2. In the callback function, you parse the response (web page) and return either dicts with extracted data, Item objects, Request objects, or an iterable of these objects. Those Requests will also contain a callback (maybe the same) and will then be downloaded by Scrapy and then their response handled by the specified callback.
3. In callback functions, you parse the page contents, typically using Selectors (but you can also use BeautifulSoup, lxml or whatever mechanism you prefer) and generate items with the parsed data.
4. Finally, the items returned from the spider will be typically persisted to a database (in some Item Pipeline) or written to a file using Feed exports.





```python
# 交互式的shell方式，你可以用它来Debug，它会返回Response对象。这需要你的系统有Ipython的环境！
scrapy shell https://www.douban.com/

# 查看response的body
response.body

# 查看response的headers
response.headers

selector属性是Selector类的实例
response.selector.xpath()
response.selector.css()

# 上面命令的简写
response.xpath()
response.css()

# 创建Scrapy工程，默认目录结构如下，scrapy.cfg文件所在的目录是工程的根目录
scrapy startproject myproject

scrapy.cfg
myproject/
    __init__.py
    items.py
    pipelines.py
    settings.py
    spiders/
        __init__.py
        spider1.py
        spider2.py
        ...

# 创建一个模板spider. template 包括： basic、crawl、xmlfeed、csvfeed
# name : 作为spider的名字。domain ： 用于生成spider的start_urls和allowed_domains属性
scrapy genspider [-t template] <name> <domain>

# 命令要放在工程内，从而模仿你spider加载网页的方式，查看headers
scrapy fetch --nolog --headers https://www.douban.com/

``` 
# 定制自己的命令

具体请参考：[Custom project commands](http://doc.scrapy.org/en/1.1/topics/commands.html#custom-project-commands)
  
  
  
