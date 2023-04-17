from  lxml import html

# 目的： 使用xpath获取html 中想要的信息

# 1. 得到页面响应内容 response.text
doc = '''
    <div>
        <ul>
            <li class="item-0">
                <a href="link1.html">first item</a>
                <a href="link1.html">123455</a>
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
# 2. 将响应内容转化为文档树对象
page = html.etree.HTML(doc)
# 3. 使用xpath
# li = page.xpath('//li')   # 获取任意的li标签
li = page.xpath('//ul/li')
# print(type(li))
print(len(li))
# 获取任意的a标签
# a = page.xpath('//a')
# a = page.xpath('//li/a')
a = page.xpath('//div/ul/li/a')
# 获取任意的a标签的href属性
# shu = page.xpath('//a/@href')
# shu = page.xpath('//a[@href]')
# print()
#获取任意的li标签的class属性
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
print(w)

# contains 函数
# it = page.xpath('//*[contains(@class,"item)]')
# starts-with
# it = page.xpath('//*[starts-with(@href,"link5)]')
# position 位置
it = page.xpath('//li[position()<3]/a/text()')
print(it)
