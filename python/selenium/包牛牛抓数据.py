"""
author: 王璐斯
file: 包牛牛抓数据.py
time: 2022/10/26 11:06
"""
from pymongo import  MongoClient
import requests
from lxml import html
def lll():
    conn = MongoClient('127.0.0.1', 27017)  # 创建连接
    db = conn.test  # 连接mydb数据库，没有则自动创建
    my_set = db.lll  # 创建数据集合 自动创建
    url = "https://www.bao66.cn/web/"
    header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)      Chrome/105.0.0.0 Safari/537.36'
}
    resp = requests.get(url, headers=header)
    resp.encoding = "utf-8"
    page = resp.text
    print(page)
    print(resp.url)

    # 获取商品的标题、简介、价格 第一页内容
    # xpath
def goods():
    # 查看五页内容
    for i in range(5):
        url = f'http://www.bao66.cn/search/web,407,钱包,,{i},5.html'

        # url = "http://www.bao66.cn/search/web,407,0,,1,5.html"
        header = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
         }
        # 请求网页
        resp = requests.get(url,headers=header)
        # a = resp.text
        # print(a)
        ht = html.etree.HTML(resp.text)
        res1 = ht.xpath('//ul[@class="product_box"]')
        print(len(lll))
        for i in res1:
            dict = {}
            name = i.xpath('.//a[@class="name"]/text()')
            if name:
                dict["name"] = name[0]
            else:
                name = ''
            title = i.xpath('.//p[@class="product_desc"]/@title')
            if title:
                dict["title"] = title[0]
            else:
                title = ''
            price = i.xpath('.//a[@class="price"]/b/text()')
            if price:
                dict["price"] = price[0]
            else:
                price = ''
            print(name, title, price)
            my_set.insert_many([dict])
goods()


