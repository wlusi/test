import urllib.parse
import urllib.request
dic = {
    "name": "王璐斯",
    "班级": "一班"
}
info = urllib.parse.urlencode(dic)  # 编码
print(info)

res1 = urllib.parse.unquote(info)  # 解码
print(res1)
url = 'http://baidu.com/s'
res2 = {"wd": "京东"}
word = urllib.parse.urlencode(res2)
new_url = url + "?" + word
header = {
   "User_Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.9071 SLBChan/8"
}
responsts = urllib.request.Request(new_url, headers=header)
response = urllib.request.urlopen(responsts)
html = response.read().decode("utf-8")
print(html)