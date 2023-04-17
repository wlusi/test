from lxml import html

# 目的： 使用xpath获取html中想要的信息
# 1. 得到网页响应内容 response.text
# 三个引号表示什么？ 注释，可以换行的字符串
doc = '''
    <div>
    <ul>
        <li class="item-0">
            <a href="link1.html">first item</a>
        </li>
        <li class="item-1">
            <a href="link2.html">second item</a>
        </li>
        <li class="item-inactive">
            <a href="link3.html">third item</a>
        </li>
        <li class="item-1">
            <a href="link4.html">fourth item</a>
        </li>
        <li class="item-0">
            <a href="link5.html">fifth item</a> 
        </li> 
    </ul>
 </div>
'''
# 2.将响应内容转化为文档树对象
page = html.etree.HTML(doc)
# 3.使用xpath
# 获取任意的li标签
# li = page.xpath('//li')
li = page.xpath('//div/ul/li')
# 获取任意的a标签
# a = page.xpath('//a')
# a = page.xpath('//li/a')
a = page.xpath('//div/ul/li/a')
# 获取任意的a标签的href属性
# shu = page.xpath('//a/@href')
# 获取任意的li标签的class属性
na = page.xpath('//li/@class')
# 获取任意的a标签的文字信息
# te = page.xpath('//a/text()')
# 获取第一个的a标签的文字信息
# te1 = page.xpath('//li/a/text()')[0]
# te1 = page.xpath('//li[1]/a/text()')
# 获取最后一个的a标签的文字信息
# wen = page.xpath('//li[last()]/a/text()')
wen = page.xpath('//li/a/text()')[-1]
# 获取最class = item-0 的li标签下的a标签的href属性
w = page.xpath('//li[@class="item-0"]/a/@href')
# class为item的ul标签下href属性为item-0的a标签的文本信息
page.xpath('//div/ul[@class="item"]/li/a[class = "item-0"]/text()')
# contains函数
e = page.xpath('//*[contains(@class,"item")]')
print(len(e))
# starts-with函数
r = page.xpath('//*[starts-with(@href,"link5")]')
print(r)
# position位置
t = page.xpath('//li[position()<3]/a/text()')
print(t)
# 1.导包
# 2.抓包
# 3.使用requests进行请求
# 4.获取响应文本信息
# 5.转换文档树类型
# 6.使用xpath匹配所需信息

