# crawl_web

用Scrapy来抓取豆瓣图书，你可以参考这个例子抓取你自己想要的网站。

**不要用它做非法的事情！！！**

___

## 版本

Python ： 2.7.10

Scrapy : 1.0.5

## 运行爬虫

    git clone https://github.com/hanxlinsist/crawl_web
    cd crawl_web/douban
    scrapy crawl douban -o books.csv -t csv

我的系统版本是ubuntu 14.04 LTS，如果你的系统是Windows，上述命令会有些差别。如果你的电脑上并没有安装Git，你可以直接下载Zip包到你的电脑上。无论如何，
你的电脑要有Python和Scrapy的安装。

上述命令运行后，会在你的当前目录下产生books.csv文件。具体内容请参考：[books.csv](https://github.com/hanxlinsist/crawl_web/blob/master/douban/books.csv)

## 定制你自己的爬虫

- scrapy startproject 你的工程名
- 在你自己工程的spiders目录下写自己的爬虫。（可以参考我的[DoubanSpider.py](https://github.com/hanxlinsist/crawl_web/blob/master/douban/douban/spiders/DoubanSpider.py)）
- 修改你自己的设置。（可以参考我的[settings.py](https://github.com/hanxlinsist/crawl_web/blob/master/douban/douban/settings.py)）

详细的设置以及代码的含义请参考：[Scrapy实战之抓取豆瓣图书](http://blog.csdn.net/xlinsist/article/details/52082626)

## 尾言

这个项目只是一个开始，还有非常多要完善的地方。如果大家对这个项目有兴趣的话，可以联系我，我们一起完善这个项目。

