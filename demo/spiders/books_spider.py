# -*- coding: utf-8 -*-
import scrapy

from demo.items import BooksItem


class BooksSpider(scrapy.Spider):

    name = 'books'
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        # xpath方法
        # for book in response.xpath('//article[@class="product_pod"]'):
        #     name = book.xpath('./h3/a/@title').extract_first()
        #     price = book.xpath('./div/p[@class="price_color"]/text()').extract_first()

        # css方法
        for book in response.css('article.product_pod'):
            item = BooksItem()
            item['name'] = book.css('h3 a::attr(title)').extract_first()
            item['price'] = book.css('p.price_color::text').extract_first()
            yield item
        # 下一页
        # next_url = response.xpath('//ul[@class="pager"]/li/a/@href').extract_first()
        next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)
