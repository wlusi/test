"""
author: 王璐斯
file: 腾讯scrapy.py
time: 2022/11/1 8:56
"""
import scrapy

class   TengXunSpider(scrapy.Spider):
    name = 'tengxun'
    allowed_domains = ["ke.qq.com"]
    start_urls = ['https://ke.qq.com/course/list?mt=1001&st=2064&page={i}']
    def parse(self, response):
        all = response.xpath('//div[!@class="course-list"]/div')
        for item in all:
            dict1 = {}
            name  = item.xpath('.//div[!@class="kc-course-card-content"]/h3/@title').extract()[0]
            link = item.xpath('.//a[@class="kc-course-card js-report-link kc-list-course-card kc-course-card kc-course-care"]').open()
