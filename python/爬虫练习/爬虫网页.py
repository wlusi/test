import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
html = response.read().decode('utf-8')
# print(html)

print(type(response))
print(response.getcode())
print(response.geturl())
print(response.info())
header = {
    "user-agent": "Mozilla/5.0()"
}
print(res1)
