"""
*_* coding: utf-8 *_*
author:zmm
time:2022/9/19 11:33
file :9.19.PY
"""
# 数据类型
name = "钢镚"
age = 3
l = 9.9
f = True
r = 2 - 2j
print(type(name), type(age), type(l), type(f), type(r))

# 列表
# 一个空列表[], 可以看做为False
list0 = []
# len(): 计算列表的长度
print(list0, len(list0))
list1 = [1, 2, 3, 4, 5]
# 遍历出列表中所有元素
for i in list1:
    print(i)
# 通过索引
print("列表1索引为0的元素是: %d" % list1[0])
# 切片
l3 = ["金", "木", "水", "火", "土"]
l1 = l3[1: 3]
print("切片后的结果: {}".format(l1))
# 列表相加
n = [1, 2, 3, 4]
name = ["西施", "昭君", "貂蝉", "玉环", "饕餮"]
print(n + name)
# enumerate(), 可以将列表索引(index)值(value)取出
# 遍历列表函数
for index, value in enumerate(name):
    print(index, value)
# append(): 添加元素, 将元素添加到列表末尾
list1 = ["喜羊羊", "懒羊羊", "沸羊羊", "慢羊羊"]
list1.append("美羊羊")
print(list1)

# 元组
# 一个元素的元组
tuple1 = (8,)
print(tuple1, type(tuple1))
t = (1)    # <class 'int'>
print(t, type(t))
# 元组取值
tuple2 = ("有点甜", "小情歌", "牛奶面包", "素颜", "年少有为", "星辰大海", "从前说")
print(tuple2[1])
print(tuple2[-1])
# 计算元组长度
index = len(tuple2) - 1
print(tuple2[index])
# 切片
print(tuple2[1:5])
print(tuple2[:])
print(tuple2[::2])

# 字典
# 空字典, <class 'dict'>
dict1 = {}
# 取值
dict2 = {"name": "章鱼哥", "age": 25}
print(dict2["name"])
print(dict2["age"])
# 添加
dict2["say"] = "蟹老板开蟹堡王"
print(dict2)
# 修改
dict2["age"] = 24
print(dict2)
# 删除数据
del dict2["say"]
print(dict2)
del dict2