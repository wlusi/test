def fun(a, b):
    i = []
    for k in range(a, b):
        if k % 4 == 0 and k % 100 != 0 or k % 400 == 0:
            i.append(k)
            # print("闰年")
        else:
            print("不是")
    print(i)
fun(998, 2021)

