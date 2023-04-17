import urllib.request
import urllib.parse
import json
# 构造request
url = "https://fanyi.baidu.com/sug"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
# post请求体
data = {
    "kw": "red"
}
info = bytes(urllib.parse.urlencode(data).encode("utf-8"))
requests = urllib.request.Request(url, data=info, headers=header)
response = urllib.request.urlopen(requests)
html = response.read().decode('utf-8')
print(json.loads(html))