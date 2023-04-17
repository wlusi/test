# 元组
tuple1 = ("窘迫", "与", "窘迫", "与", "窘迫", "与")
print(tuple1)
# 获取索引
print(tuple1.index("与"))
# 获取次数
print(tuple1.count("与"))
# 列表转元组
io = tuple(m)
print(io)
yu = io + tuple1
print(yu)
print("--------------------------------------")
