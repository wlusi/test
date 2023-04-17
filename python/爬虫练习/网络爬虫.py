"""
author: 王璐斯
file: 网络爬虫.py
time: 2023/1/7 17:22
"""
import requests
from lxml import html
url = 'https://b.faloo.com/y_0_1.html'
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

res = requests.get(url, header)
respon = res.text
page = html.etree.HTML(respon)
res1 = page.xpath('//div[@class="centerTwo bodyBorderShadow"]/div[@id="BookContent"]//div[@class="TwoBox02_02"]')
for i in res1:
                title = i.xpath('.//div[@class="TwoBox02_03"]//a/@title')[0]
                img = i.xpath('.//div[@class="TwoBox02_03"]//img/@src')[0]
                print(title, img)
                w = requests.get(img)
                if w.status_code == 200:
                    with open('./img/' + str(title) + '.jpg', 'wb')as f:
                        f.write(w.content)