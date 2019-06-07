# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    cname = scrapy.Field()  # 分类名称
    name = scrapy.Field()
    img_url = scrapy.Field()
    pass


class AutoLogosItem(scrapy.Item):  # 车标
    cname_en = scrapy.Field()  # 国产车标英文：guochan
    cname_zn = scrapy.Field()  # 国产车标中文名
    name = scrapy.Field()      # 汽车名
    img_url = scrapy.Field()   # 车标url


class BooksItem(scrapy.Item):  # 书
    name = scrapy.Field()
    price = scrapy.Field()
