"""
author: 王璐斯
file: 抖音.py
time: 2022/10/20 10:57
"""
import requests
import json
url = 'https://www.douyin.com/aweme/v1/web/hot/search/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&detail_list=1&source=6&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=106.0.0.0&browser_online=true&engine_name=Blink&engine_version=106.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7156421846455682591&msToken=MizxdF_J4PHr601Hd0FQNFe4iWqUk8XSy814RGxhw-6kM59lFzx8zWOpyjl7Z03vZQ2cfButAzLY7bCQ3h_TUkqklPn3XvOWStGEcaxgLVldvigndMh9&X-Bogus=DFSzswVYXTsANxA7S/vSGRXAIQ5I'
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
'referer': 'https://www.douyin.com/discover'
}
res = requests.get(url, headers=header)
# 获取网页源码
page = res.text
# print(page)  # 字符串
info = json.loads(page)
# print(info)  # 字典类型
# print(type(page), type(info))
# 字典取值
word_list = info['data']['word_list']  # info['data']

# print(len(word_list))
for item in word_list:
    word = item['word']
    print(word)
