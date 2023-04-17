import requests
import json
# 登录url
url1 = 'https://accounts.douban.com/'
# 请求头
headers = {""
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"

}

#  参数
data = {
    "remember": "true",
    "name": "17589526243",
    "password": "W.ls200313",
}
# 创建session对象；保持会话
session = requests.session()
res = session.post(url1, params=data, headers=headers)
print(res.text)

header2 = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
url2 = 'https://www.douban.com/people/210071258'
res3 = session.get(url2, data=data,  headers=header2)
print(res3.text)
