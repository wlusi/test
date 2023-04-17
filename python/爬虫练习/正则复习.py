import re
# 你好，hello, 世界  从该字符串中提取中文数据
text = '你好, hello, 世界'
# 1.通过正则表达式，生成一个Patten对象
res1 = re.findall('[\u4e00-\u9fa5]+', string='你好, hello, 世界')
print(res1)
ret = re.findall('情', '速度情与激情10')
print(ret)
s1 = '阅读量9999, 点赞数1110'
a = re.findall('\d', s1)
print(a)
a1 = re.findall('\d+', s1)
print(a1)
# 练习1：把一个字符串中非数字的内容拼成一个字符串
# # 例如输入的是 a1b2c3----输出"abc"
# str1 = input("输入一个字符串：")
res2 = re.findall('[a-zA-Z]', string="a1b2c3")
res02 = "".join(res2)
print(res02)
# 方法2：
str1 = input("输入一个字符串：")
re3 = re.findall('[^0-9]', string=str1)
re03 = "".join(re3)
print(re03)