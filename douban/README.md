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

``` 
  
  
  
  
