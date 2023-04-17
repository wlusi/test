import json
s = '中文123abc'
a = json.dumps(s)
print(json.loads(a))

d = {'name': '张三'}
b = json.dumps(d)
print(b)

# 1.json 花括号，双引号
# 2.内置模块，不需要安装，可以直接导入使用
# 3.内置四个方法 dump()dumps()load()loads()