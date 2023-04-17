import scrapy


class ChinazSpider(scrapy.Spider):
    name = 'chinaz'
    allowed_domains = ["chinaz.com"]
    start_urls = ['http://top.chinaz.com/hangye/']

    def parse(self, response):
        # 解析数据直接用response.xoath()
        # 不请求不转化文档数对象直接用就行
        all = response.xpath('//ul[@class="listCentent"]/li')
        for item in all:
            name = item.xpath('.//h3[@class="rightTxtHead"]/a/@title').extract()[0]
            link = item.xpath('.//h3[@class="rightTxtHead"]/span/text()').extract()[0]
            info = item.xpath('.//p[@class="RtCInfo"]/text()').extract()[0]
            paming = item.xpath('.//div[@class="RtCRateCent"]//strong/text()').extract()[0]
            print(name,link,info,paming)



        pass
