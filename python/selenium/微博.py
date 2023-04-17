"""
author: 王璐斯
file: 微博.py
time: 2022/10/20 11:21
"""
import requests
import json
import re
import csv
url = 'https://weibo.com/ajax/statuses/topic_band?sid=v_weibopro&category=all&page=1&count=10'
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
# link = f'link = f"https：//s.weibo.com/weibo?q={name}&topic_ad="'
response = requests.get(url, headers=header)
requests.enconing = 'utf-8'
res = response.text
info = json.loads(res)
with open('ls.csv', 'a+', newline='') as f:
    obj = csv.writer(f)
    row = ['排名', '姓名', '阅读量', '讨论量']
    obj.writerow(row)
# 获取网页数据
# page = json.loads(info)
# 字典取值
# print(info)
    cate_list = info['data']['statuses']
    for item in cate_list:
        word = item['word']
        label_name = item['label_name']
        # topic = item['rank']
        # name = item['topic']
        # read = item['read']
        # mention = item['mention']
        # print(topic, name, read, mention, images_url)
        a = [item['rank'], item['topic'], item['read'], item['mention']]
        obj.writerow(a)

