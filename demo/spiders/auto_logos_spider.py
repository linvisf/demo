# -*- coding: utf-8 -*-
"""
目标网址：https://www.pcauto.com.cn/zt/chebiao/
目标：下载车标，并以汽车品牌命名，以不同国家产的汽车作为文件夹
需求分析：
1、提取数据，品牌名，车标url,
    不同国家产的汽车名，有中文名和英文名，看自己是想用哪个作为文件夹名称
    分析这几个字段在网页结构，便于通过xpath或css提取
2、下载图片，自定义图片名字
"""
import scrapy

from demo.items import AutoLogosItem


class AutoLogosSpider(scrapy.Spider):

    name = 'autologos'
    start_urls = [
        'https://www.pcauto.com.cn/zt/chebiao/guochan/',
        'https://www.pcauto.com.cn/zt/chebiao/riben/',
        'https://www.pcauto.com.cn/zt/chebiao/deguo/',
        'https://www.pcauto.com.cn/zt/chebiao/faguo/',
        'https://www.pcauto.com.cn/zt/chebiao/yidali/',
        'https://www.pcauto.com.cn/zt/chebiao/yingguo/',
        'https://www.pcauto.com.cn/zt/chebiao/meiguo/',
        'https://www.pcauto.com.cn/zt/chebiao/hanguo/',
        'https://www.pcauto.com.cn/zt/chebiao/qita/',
    ]

    def parse(self, response):
        li_list = response.css('ul.expPicA li')
        for li in li_list:
            item = AutoLogosItem()
            item['cname_en'] = response.url.split('/')[-2]  # guochan
            item['cname_zn'] = response.css('span.mark a::text').extract_first()  # 国产车标
            item['name'] = li.css('div.dTxt a::text').extract_first()
            img_url = li.css('i.iPic img::attr(src)').extract_first()
            img_url = 'http:' + img_url
            item['img_url'] = [img_url]  # img_url不要少了[]
            yield item
