# -*- coding: utf-8 -*-
import scrapy

from demo.items import DemoItem


class DemoSpider(scrapy.Spider):

    name = 'demo'

    allowed_domains = ["pic.netbian.com"]

    start_urls = [
        'http://pic.netbian.com/4kfengjing/',
        'http://pic.netbian.com/4kmeinv/',
        'http://pic.netbian.com/4kyouxi/',
        'http://pic.netbian.com/4kdongman/',
        'http://pic.netbian.com/4kyingshi/',
        'http://pic.netbian.com/4kmingxing/',
        'http://pic.netbian.com/4kqiche/',
        'http://pic.netbian.com/4kdongwu/',
        'http://pic.netbian.com/4krenwu/',
        'http://pic.netbian.com/4kmeishi/',
        'http://pic.netbian.com/4kzongjiao/',
        'http://pic.netbian.com/4kbeijing/',
    ]

    def parse(self, response):
        li_list = response.css('div.slist li')
        for dd in li_list:
            item = DemoItem()
            item['cname'] = response.url.split('/')[-2]  # 分类名称
            item['name'] = dd.css('b::text').extract_first()
            img_url = dd.css('img::attr(src)').extract_first()
            src = 'http://pic.netbian.com' + img_url
            item['img_url'] = [src]
            yield item

        next_url = response.xpath('//div[@class="page"]/a[text()="下一页"]/@href').extract_first()
        if next_url:
            yield response.follow(next_url, callback=self.parse)

