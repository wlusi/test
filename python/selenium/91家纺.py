"""
author: 王璐斯
file: 91家纺.py
time: 2022/11/23 11:17
"""
import csv
import requests
from lxml import html
url = "http://www.91jf.com/"
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
respons = requests.get(url, headers=header)
respons.encoding = 'utf-8'
jia = respons.text
add = html.etree.HTML(jia)
res = add.xpath('//div[@class="index_g_class"]/ul/li')
with open('jia.csv', 'a+', newline='') as f:
    obj = csv.writer(f)
    for i in res:
        add1 = i.xpath('.//div[@class="class_menu"]/a/span/text()')[0]
        add2 = i.xpath('.//div[@class="class_menu"]/a/text()')[0]
        add3 = i.xpath('.//div/ul/li')
        for e in add3:
            add4 = e.xpath('.//a/span/text()')[0]
            info = [add1, add2, add4]
            obj.writerow(info)