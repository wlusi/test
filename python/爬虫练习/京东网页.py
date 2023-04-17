import requests
from lxml import html
url = 'https://www.jd.com'
response = requests.get(url)
# print(response.text)
html = html.etree.HTML(response.text)
data = html.xpath('//li[@ class="cate_menu_item"]/a/text()')
print(data)