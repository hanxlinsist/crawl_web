# 介绍

这个项目主要用Scrapy抓取目标网站，每个目录下都抓取特定的网站。由于网站类型不同，因此每个特定的spider都有不一样的功能，不同的配置，不同过滤数据的方式。当然了，参照这个仓库的例子，你完全可以定制你自己的爬虫，抓取你自己想要的网站。

___

# 版本

下面，是我写这个项目时用到的版本：

Python : **2.7.12**

Scrapy : **1.1.0**

numpy : **1.11.1**


# 运行爬虫

**对应的目录有相应的运行说明**

    git clone https://github.com/hanxlinsist/crawl_web
    cd crawl_web/douban
    scrapy crawl douban -o books.csv -t csv

我的系统版本是ubuntu 14.04 LTS，如果你的系统是Windows，上述命令会有些差别。如果你的电脑上并没有安装Git，你可以直接下载Zip包到你的电脑上。无论如何，
你的电脑要有Python和Scrapy的安装。

上述命令运行后，会在你的当前目录下产生books.csv文件。具体内容请参考：[books.csv](https://github.com/hanxlinsist/crawl_web/blob/master/douban/books.csv)

# 高级特点

1. 代理IP抓取目标网站
2. 定制自己的请求客户端
3. 一个项目下的pipelines只过滤相应的Item

## 尾言

这个项目只是一个开始，还有非常多要完善的地方。如果大家对这个项目有兴趣的话，可以联系我，我们一起完善这个项目。

