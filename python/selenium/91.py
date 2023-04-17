"""
author: 王璐斯
file: 91.py
time: 2022/11/23 12:19
"""
import requests
from lxml import html

url = 'http://www.91jf.com/'
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
res = requests.get(url, headers=header)
res.encoding = 'utf-8'
res = res.text
# print(res)
info = html.etree.HTML(res)
cate = info.xpath('//div[@class="index_g_class"]/ul/li')
for i in cate:
    cate1 = i.xpath('.//div[@class="class_menu"]/a/span/text()')[0]
    cate2 = i.xpath('.//div[@class="class_menu"]/a/text()')[0]
    cate_3 = i.xpath('.//div/ul/li')
    for it in cate_3:
        cate3 = it.xpath('.//a/span/text()')[0]
        print(cate1, cate2, cate3)