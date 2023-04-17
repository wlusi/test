import requests
from lxml import html
url = 'https://www.hc360.com/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=header)
response.encoding = 'utf-8'
html = html.etree.HTML(response.text)
cates = html.xpath('//dd[@class="aside-dd"]/dl')  # 所有的类目 12个 包含一级类目 二级类目 三级类目
for cate in cates:
    print(cate)
    cate1 = cate.xpath('.//dt/span/text()')  # 一级类目
    cate_li = cate.xpath('.//dd/dl')  # 包含所有三级类目的二级类目列表
    for i in cate_li:
        dict = {}
        cate2 = i.xpath('.//dt/text()')  # 二级类目
        # cate3 = i.xpath('.//dd/a/text()')
        cate3 = i.xpath('.//dd/a')  # 三级类目
        for j in cate3:
            cate3l = j.xpath('.//text()')
            dict['cate1'] = cate1  # 一级类目
            dict['cate2'] = cate2
            dict['cate3'] = cate3l
            print(dict)
print('###########################')