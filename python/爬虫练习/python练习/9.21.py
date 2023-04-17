# 写一个函数，实现输出公元998--2020年之间的所有闰年，要求如果闰年存在，则输出所有闰年，如果该区间不存在闰年，则输出该区间不存在闰年。
def fun(a,b):
    list1 = []
    for i in range(a,b):
        if i % 4 == 0 and i % 100 !=0 or i == 0:
            list1.append(i)
            print("是闰年")
        else:
            print(i, "我不是闰年")
fun(998,2021)