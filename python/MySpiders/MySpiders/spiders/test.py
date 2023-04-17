import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['chinaz.com']
    start_urls = ['http://chinaz.com/']

    def parse(self, response):
        pass
