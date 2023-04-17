# My_str = ‘11sdsfsdf45sfxcv67qwe_9’ 手写一个函数，计算出字符串中所有数字的和
# sum = 0
# My_str = "11sdsfsdf45sfxcv67qwe_9"
# for i in My_str:
#     if i.isdigit():
#         # print(i)
#         i = int(i)
#         sum += i
# print(sum)
# # 手写一个函数，将 ’hello xiao mi’ 作为参数输入，函数返回 ‘mi xiao hello’，注意是单词位置颠倒，而不是字母位置颠倒
# q1 = "hello xiao mi"
# def fun():
#     # 分割函数
#     q = q1.split(" ")
#     q.reverse()
#     print(''.join(q))
# fun()
#
# # 5．str = ‘那车水马龙的人世间,那样地来 那样地去,太匆忙’ 写一个函数，输出最后一次出现"那"的下标。
# str = '那车水马龙的人世间,那样地来,那样地去,太匆忙'
# # s = str.rfind("那")
# # print(s)
# sum = 0
# while sum < len(str):
#     for i in str:
#         if i == "那":
#             sum += 1
#             print(sum)
#     break
# print("------------------------------")
# # 6．Str = ‘123.py’ 或者 str = ‘123.json’ 写一个函数，判断一个字符串是否以.py结束
# str = "123.json"
# s = ".py"
# if str[3::1] == s:
#     print("是")
# else:
#     print("否")
# # 7．str = " fgh " 写一个函数，只去掉字符串右侧的空格，左侧的空格保留
# str = " fgh "
# s = str.rstrip()
# print([s])
# # 8．写一个函数可以将一个字符串右移n位,例如 “hello world” 右移两位后ldhello wor
# # str = "hello world"  # ldhello wor
# # a = int(input("请选择位移的个数："))
# # s = str[-a::1]
# # z = str[:-a:1]
# # b = s + z
# # print(b)
# # 之间是否存在回文数，如果存在输出全部回文数及其数量，如果不存在，则输出该区间不存在回文数（回文数：正着读和反着读相同的数例如：171 / 181）
# #判断回文数
# # def fun2():
# #     sum = 0
# #     for i in range(10000, 15001):
# #         if int(i) == int(i)[::-1]:
# #             print(i, end=" ")
# #             sum += 1
# #     if sum == 0:
# #         print("没有回文数")
# #     print(sum)
# # fun2()
#
#
#
# # my_str = ‘123.json’ 写一个函数，判断字符串是否以”.json”结束,如果是以”.json”,要求将“.json”替换为“.py987”，并输出my_str中非空白字符数量
# def get_lo():
#     my_str = "123.json"
#     if my_str.endswith(".json"):   # 判断结尾
#         l = my_str.replace('.json', '.py987')    # 替换
#         if not my_str.isspace():    # 判断是否为空白字符
#             print(l)
# get_lo()
# #  请手写一个函数，某个字符串为“abc102324123499123ABC”，计算该字符串中所有数字之和以及字母的数量
# sum = 0
# list1= []
# My_str = "abc102324123499123ABC"
# for i in My_str:
#     if i.isdigit():
#         # print(i)
#         i = int(i)
#         sum += i
#     elif i.isalpha():
#         list1.append(i)
#         print(list1)
# print(sum, len(list1))

# 请手写一个函数，创建一个空列表alist，使用随机数模块随机生成10个整数，数字范围在[11-111] 这个区间，并将生成的10个随机数全部添加到alist中，添加完成后，求输出所有随机数之和。
# def fun3():
#     alist = []
#     for j in range(11, 112):
import random  # 引入导包
# alist = [random.randint(11, 111) for i in range(10)]  # 用列表生成式添加数，random.randint(1,10)是循环体
# print(alist)
# f = sum(alist)
# print(f)
# def m():
#     alist = []
#     for i in range(10):
#         a = random.randint(11, 111)
#         i = a
#         alist.append(i)
#     b = sum(alist)
#     print(b)
#     print(alist)
# m()
# # 随机生成一个加上1添加到新列表中
# list1 = [1, 2, 3, 4]
# list2 = []
# for i in list1:
#     i += 1
#     list2.append(i)
# print(list2)
# print("--------------------")
# # while循环实现
# list3 = []
# i = 2
# while i < 6:
#     list3.append(i)
#     i += 1
# print(list3)
# print("----------------------------")
# # 3 map函数 lambda匿名函数
# d = map(lambda k: k+1, list1)
# print(list(d))
# print("-------------------")
# # 4列表推导式
# f = [j + 1 for j in list1]
# print(f)
# 请写一个函数，实现向“test.txt”文件中写入两行数据，第一行写入数据“hello world”，第二行写入“hello python”
import random
#
# with open('text.txt', mode='w+', encoding="utf-8") as f:
#     f.write('hello world\nhello python')
# # f.seek(0)
# # print(f.readlines())
# f.close()
# with open('text.txt', mode='r', encoding="utf-8") as m:
#     o = m.readlines()
#     print(o)
# m.close()
# # a = [“张三”,”张四”,”张五”,”王二”] 如何删除姓张的
# # a = ["张三", "李四", "张五", "王二"]
# # list5 = []
# # list6 = []
# # for name in a:
# #     if name.startswith('张'):
# #         list5.append(name)
# #         if not list5:
# #             list6.append(a)
# # print(list6)
#
# a = ["张三", "张四", "张五", "王二"]
# def fun3(b):
#     return b[0] != '张'
# w = list(filter(fun3, a))  # 过滤器filter
# print(w)
# # 高阶函数(map,filter,reduce)
# from functools import reduce    # python2以下需要导入
# def fun4(x, y):
#     return x*2+y
# a = reduce(fun4,[1,2,3,4])
# print(a)
# 手写一个函数，将str1 = “hda48465#da4@89d8a_”作为参数传入，找出整个字符串中出现次数最多的字母，输出该字母和她出现的次数

def fun5():
    c = []
    str1 = "hda48465#da4@89d8a_"
    for x in str1:
        if x.isalpha():
            c.append(x)
    print(c)
    v = set(c)
    print(v)
    for j in v:
        num = c.count(j)
        if num > 1:
            print(j, num)
        pass
fun5()
# 手写一个函数，实现五次登录机会，如果用户输入的用户名为admin，密码为admin123，则登陆成功并终止程序，否则，登陆失败并告诉用户还有几次登陆机会
count = 5
for i in range(6):
    name = input("请输入用户名：")
    pw = input("请输入用户密码：")
    if (name == 'admin')and (pw =='admin123'):
        print('登录成功')
        break
    else:
        count = count-1
        print(f'密码不对，请重新输入，还有{count}次机会')
else:
    print('超过五次，登录失败')

