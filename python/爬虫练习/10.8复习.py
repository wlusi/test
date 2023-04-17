import requests
from lxml import html
# url = 'http://www.zhubaojie.com/'
# resp = requests.get(url)
# html = html.etree.HTML(resp.text)
# a = html.xpath('//ul[@class="site-menu"]/li/a/text()')
# print(a)
url = 'http://www.hc360.com/'
resp = requests.get(url)
html = html.etree.HTML(resp.text)
a = html.xpath('//ul[@class="sub-menu-dt"]/li/a/text()')
print(a)