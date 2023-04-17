"""
author: 王璐斯
time: 2022/9/21 15:35
file: 练习题.py
"""
# 1.写一个函数，实现输出公元998--2020年之间的所有闰年，要求如果闰年存在，则输出所有闰年，如果该区间不存在闰年，则输出该区间不存在闰年。
def year(y1, y2):
    l = []
    for i in range(y1, y2):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            l.append(i)
            print("是闰年")
        else:
            print("不是闰年")
    print(l, "区间内所有的闰年")
year(998, 2020)

#2.请手写一个函数，用来取出1-100（均包含）中3的倍数或者带有数字3的所有整数
def num():
    l1 = []
    for i in range(1, 101):
        if i % 3 == 0 or i // 10 == 3:
            l1.append(i)
    print(l1)
num()
def fun():
    for i in range(1, 101):
        if i % 3 == 0 or '3' in str(i):
            print(i)

# 3.My_str = ‘11sdsfsdf45sfxcv67qwe_9’ 手写一个函数，计算出字符串中所有数字的和
My_str = '11sdsfsdf45sfxcv67qwe_9'
sum = 0
i = []
for i in My_str:
    if i.isdigit():
        i = int(i)
        sum += i
print(sum)

# 4.手写一个函数，将 手写一个函数，将 ’hello xiao mi’ 作为参数输入，函数返回 ‘mi xiao hello’，注意是单词位置颠倒，而不是字母位置颠倒
def h(z):
    if z:
        m = z.split()
        m.reverse()
        print(''.join(m))
h(z = 'hello xiao mi')

# 5.str = '那车水马龙的人世间,那样地来 那样地去,太匆忙' 写一个函数，输出最后一次出现"那"的下标
def t():
    str = '那车水马龙的人世间,那样地来 那样地去,太匆忙'
    a = str.rindex('那')
    # a = str.rfind('那')
    print(a)
    pass
t()
def fun():
    dic = {}
    str = '那车水马龙的人世间,那样地来 那样地去,太匆忙'
    # 方法一
    a = [i for i in str]
    print(a)
    length = len(str)
    b = [j for j in range(length)]
    print(b)
    for j in range(length):
        dic.update({str[j]:j})
        pass
    for i in dic:
        # print(i, dic[i])
        pass
    # 方法二
    for k, v in enumerate(str):
        if v == '那':
            print(k)
fun()

# 6.写一个函数，实现判断100-150之间是否存在回文数，如果存在输出全部回文数及其数量，如果不存在，则输出该区间不存在回文数（回文数：正着读和反着读相同的数例如：171/181）
def h(a, b):
    list1 = []
    for i in range(a, b):
        if (i // 100 % 10 == i // 10 % 10) and (i // 1000 == i % 10):
            list1.append(i)
    print(list1)
h(1000, 1500)
def hui():
    sum = 0
    for i in range(1000, 1501):
        if str(i) == str(i)[::-1]:
            print(i, end=" ")
            sum += 1
    if sum == 0:
        print("没有回文数")
    print(sum)
hui()

# 7.my_str = ‘123.json’ 写一个函数，判断字符串是否以”.json”结束,如果是以”.json”,要求将“.json”替换为“.py987”，并输出my_str中非空白字符数量
def m():
    my_str = '123.json'
    sum = 0
    flag = my_str.endswith('.json')
    if flag:
        str = my_str.replace('.json', '.py987')
        for i in str:
            if i.isspace():
                continue
            else:
                sum += 1
        print(sum)
    pass
m()

# 8.请手写一个函数，某个字符串为“abc102324123499123ABC”，计算该字符串中所有数字之和以及字母的数量
def fun():
    sum = 0
    list = []
    s = "abc102324123499123ABC"
    for i in s:
        if i.isdigit():
            sum += int(i)
            pass
        elif i.isalpha():
            list.append(i)
    print(sum, len(list))
fun()

# 9.请手写一个函数，创建一个空列表alist，使用随机数模块随机生成10个整数，数字范围在[11-111] 这个区间，并将生成的10个随机数全部添加到alist中，添加完成后，求输出所有随机数之和。
import random
def math():
    alist = []
    for i in range(10):
        n = random.randint(11, 112)
        i = n
        alist.append(i)
    # b = sum(alist)
    print(alist)
    # print(b)
math()

# 10.[1,2,3,4]变成[2,3,4,5]
a = [1, 2, 3, 4]
l2 = []
# 遍历
for i in a:
    i = i + 1
    l2.append(i)
print(l2)
# 列表推导式
z = [j + 1 for j in a]
print(z)
# map函数，lambda匿名函数
d = map(lambda  k : k + 1, a)
print(list(d))
def z():
    a = [1, 2, 3, 4]

# 11.请写一个函数，实现向“test.txt”文件中写入两行数据，第一行写入数据“hello world”，第二行写入“hello python”
def wj():
    with open("test.txt", mode="w+", encoding="utf-8") as f:
        f.write("hello world \n hello python")
        f.seek(0)
        print(f.read())
wj()

# 12.a = [“张三”,”张四”,”张五”,”王二”] 如何删除姓张的
a = ["张三", "张四", "张五", "王二"]
def fun(b):
    return b[0] != '张'
print(list(filter(fun, a)))