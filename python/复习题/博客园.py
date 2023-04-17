"""
author: 王璐斯
file: 博客园.py
time: 2022/11/2 8:45
"""
import csv
import requests
from lxml import html
#  https://www.cnblogs.com/AggSite/AggSitePostList
url = 'https://www.cnblogs.com/'
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=header)
response.encoding = 'utf-8'
page = html.etree.HTML(response.text)
# https://www.cnblogs.com/#p2
# https://www.cnblogs.com/#p3
with open("wls.csv", "a+", newline="", encoding='utf-8-sig') as f:
    obj = csv.writer(f)
    row = ["名字", "链接"]
    obj.writerow(row)
    for i in range(1, 4):
        page_link = url + '#p' + str(i)
        res = requests.get(page_link, headers=header)
        res.encoding = 'utf-8'
        page1 = html.etree.HTML(res.text)
        course_li = page1.xpath('//div[@class="post-list"]/article/section/div')
        for course in course_li:
            name = course.xpath('.//a/text()')
            link = course.xpath('.//a/@href')
            obj.writerow([name, link])





