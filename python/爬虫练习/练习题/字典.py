# 字典
key1 = {"小红": 1, "小明": 2, "小花": 3}
print(key1)
# 字典的遍历
# 利用循环语句和字典的items()方法
# 格式: 字典名.items()
key1 = {"小红": 1, "小明": 2, "小花": 3}
for key, value in key1.items():
    print(key, value)
for key2 in key1.keys():
    print(key2)
# update():将一个字典合并到另一个字典中
dict1 = {1: 100, 2: 200}
dict1.update(key1)
print(dict1)