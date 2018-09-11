# # -*- coding: utf-8 -*-
# import scrapy
# import requests
# import  re

#
# # class InformationSpider(scrapy.Spider):
# #     name = 'information'
# #     allowed_domains = ['zhaopin.com']
# #     start_urls = ['http://zhaopin.com/?pageSize=60&jl=489&kw=爬虫&kt=3']


import scrapy
from scrapy_splash import SplashRequest
from  zhilian.items import ZhilianItem


class InformationSpider(scrapy.Spider):
    name = 'information'
    allowed_domains = ['zhaopin.com']
    start_urls = ['https://sou.zhaopin.com/?p=2&pageSize=60&jl=489&kw=%E7%88%AC%E8%99%AB&kt=3/js']
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse)

    def parse(self, response):
        for x  in response.xpath("//div[@id='listContent']/div").extract_first() :
            name = x.xpath("//span[@title]/text()").extract_first()
            salary = x.xpath("//p[@class='job_saray']/text()").extract_first()
            company = x.xpath("//*[@class='company_title']/text()").extract_first()
            city = x.xpath("//ul/li[@class='demand_item']/text()").extract_first()
            welfare = x.xpath("//div[@class='welfare_item']/text()").extract()
            url =x.xpath("//div[@class='commpanyName']/a/@href").extract()
            item = ZhilianItem()
            item['name'] = name
            item['salary'] = salary
            item['company'] = company
            item['city'] = city
            item['welfare']=welfare
            item['url'] = url
            yield item


