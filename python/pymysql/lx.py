"""
author: 王璐斯
file: lx.py
time: 2022/10/13 14:55
"""
import requests
from lxml import html
url = ''

class Hui(object):
    def __init__(self):
        self.header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
        self.url = 'https://www.hc360.com/'
