 # 列表
m = ["学习", 1, 2, 3, 4, 5, 4, 3, 2, 1]
print(m, type(m))
i = m[0]
print(i)
m.append(10)
print(m)
# m.extend(20)
m.insert(2, 20)
print(m)
# 删(remove, pop, clear)
print(m.remove(1))
# 改
m[0] = 2
print(m)
# 查
m.index(5)
print(m.index(5))
print("-------------------------")









