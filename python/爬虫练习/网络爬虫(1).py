"""
author: 王璐斯
file: 网络爬虫(1).py
time: 2023/2/20 13:30
"""
import requests
from lxml import html
url = 'https://b.faloo.com/y_0_1.html'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
res =requests.get(url, headers=header)
respon = res.text
page = html.etree.HTML(respon)