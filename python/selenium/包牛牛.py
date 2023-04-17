"""
author: 王璐斯
file: 包牛牛.py
time: 2022/10/26 9:34
"""
import requests
from lxml import html
url = "http://www.bao66.cn/search/web,407,0,,1,5.html"
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
respons = requests.get(url, headers=header)
respons.encoding = 'utf-8'
add = html.etree.HTML(respons.text)
res = add.xpath('//ul[@class="product_box"]')
res1 = res[0]
for a in res1:
    name = a.xpath('.//div/p/@title')
    img = a.xpath('.//p/a[@target="_blank"]/text()')
    jiage = a.xpath('.//p[@class="desc_hover"]//b/text()')
    print(name, img, jiage)  


