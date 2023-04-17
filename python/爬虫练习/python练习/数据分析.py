"""
author: 王璐斯
file: 数据分析.py
time: 2023/1/7 19:29
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['fangsong']
plt.rcParams['figure.figsize'] = (3, 4)
plt.rcParams['figure.dpi'] = 200
# 1. 创建一个30个元素的数组分别改变成两个形状（5,6）（6,6）
one = np.arange(30)
print(one)
print("***************************")
# 改变形状 （5,6）
two = one.reshape(5, 6)
print(two)
print("***************************")
# 改变形状为（6,6）
a = np.resize(one, (6, 6))
print(a)
# 1.提取出数组中所有奇数
# 2.修改奇数值修改为-1
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# 1.提取出数组中所有奇数
# 方法1
for i in x:
    for it in i:
        if it % 2 != 0:
            print(it)
print("^^^^^^^^^^^^^^^^^^^^^")
# 2.修改奇数值修改为-1
# 方法1
for i in x:
    for it in i:
        if it % 2 != 0:
            it = -1
            print(it)
print("%%%%%%%%%%%%%%%%%%%%%")
# 创建一个从0-100之间的随机生成一个一维数组并进行倒叙复制给另一个元素
# 方法1
b = np.arange(10, 49)
print(b)
c = b[::-1]
print(c)
# 方法2
temp = np.copy(b[::-1])
print(temp)
# 4.使用随机函数，在0-100之间随机生成一个一维数组有5个元素
d = np.random.randint(100, size=(5,))
print(d)
print(d.shape)  # 元素个数
print(d.ndim)  # 一维数组
# 变化数组使用添加的方法
a = [[1,2,3],[4,5,6]]
print(a)
# 方法1
a.append([7, 8, 9])
print(a)
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
# 删除的原则遵循0行1列的原则即可
print(np.delete(a, 2, axis=1))
print(np.delete(a, 2, axis=0))
#        第一天票房 第二天票房 第三天票房
# 想见你      3100      5878     5500
# 阿凡达:水之道 4000    6795    5678
# 绝望主夫   3560          4599    5600
# 按照以上数据 1.绘画同位置多柱状图
#  1.绘画同位置多柱状图
movies = ["想见你", "阿凡达:水之道", "绝望主夫"]
# y轴数据
data1 = [3100, 4000, 3560]
data2 = [5878, 6795, 4599]
data3 = [5500, 5678, 5600]
width = 0.3
x = np.arange(len(movies))
# x轴
day1 = x
day2 = x+width
day3 = x+2*width
plt.bar(day1, data1, color='r', width=width)
plt.bar(day2, data2, color='c', width=width)
plt.bar(day3, data2, color="m", width=width)
# 设置x轴的信息 美化x轴
plt.xticks(x+width, labels=movies, color='b')
#显示文本信息
for i in range(len(movies)):
    plt.text(day1[i], data1[i], data1[i], va='bottom', ha='center')
    plt.text(day2[i], data2[i], data2[i], va='bottom', ha='center')
    plt.text(day3[i], data3[i], data3[i], va='bottom', ha='center')
# 设置图例
label = ["第一天", "第二天", "第三天"]
plt.legend(labels=label)
plt.show()
# 2. 绘制堆叠图
movies = ["想见你", "阿凡达:水之道", "绝望主夫"]
# y轴数据
data1 = np.array([3100, 4000, 3560])
data2 = np.array([5878, 6795, 4599])
data3 = np.array([5500, 5678, 5600])
width = 0.3
x = np.arange(len(movies))
plt.bar(movies, data1, bottom=data2+data3, color='red',width=width, label="第一天票房")
plt.bar(movies, data2, bottom=data3, color='blue', width=width, label="第一天票房")
plt.bar(movies, data3, color='m', width=width, label="第二天票房")
# 设置文本的信息
for i in range(len(movies)):
    max_y = data1[i]+data2[i]+data3[i]
    plt.text(movies[i], max_y, max_y, va='bottom', ha='center')
# 设置图例
plt.legend()
plt.show()
movies = ["想见你", "阿凡达:水之道", "绝望主夫"]
# y轴数据
data1 = [3100, 5878, 5500]
data2 = [4000, 6795, 5678]
data3 = [3560, 4599, 5600]
width = 0.3
x = np.arange(len(movies))
# x轴
day1 = x
day2 = x+width
day3 = x+2*width
plt.bar(day1, data1, color='r',  width=width)
plt.bar(day2, data2, color='c', width=width)
plt.bar(day3, data2, color="m", width=width)
# 设置x轴的信息 美化x轴
plt.xticks(x+2*width, labels=movies, color='b')
# 显示文本信息
for i in range(len(movies)):
    plt.text(day1[i], data1[i], data1[i], va='bottom', ha='center')
    plt.text(day2[i], data2[i], data2[i], va='bottom', ha='center')
    plt.text(day3[i], data3[i], data3[i], va='bottom', ha='center')
# 设置图例
label = ["想见你  ", "阿凡达:水之道", "绝望主夫"]
plt.legend(labels=label)
plt.show()
#  某家庭的八月份支出 娱乐 育儿 饮食 房贷 交通 其他
#                       200 500 1200 7000  200   900
plt.rcParams['figure.figsize'] = (6, 4)
labels = ["娱乐", "育儿", "饮食", "房贷", "交通", "其他"]
x = [200, 500, 1200, 7000, 200, 900]
# 基本绘制
info = plt.pie(x, labels=labels)
m = plt.pie(x, labels=labels, autopct='%.2f%%')
plt.title("饼图示例-8月份家庭支出", fontsize=18)
print(m)