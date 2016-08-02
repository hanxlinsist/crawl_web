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

上述命令运行后，会在你的当前目录下产生books.csv文件。具体内容请参考：![books.csv](https://github.com/hanxlinsist/crawl_web/blob/master/douban/books.csv)





