import urllib.request
import urllib.parse
import json
url = ''
header = {
    "Request URL": "https://pagead2.googlesyndication.com/getconfig/sodar?sv=200&tid=gda&tv=r20220922&st=env"
}
data = {
    "remember": "true",
    "name": "17589526243",
    "password": "123456"
}
info = bytes(urllib.parse.urlencode(data).encode("utf-8"))

requests = urllib.request.Request(url, data=info, headers=header)
response = urllib.request.urlopen(requests)
print(response.read().decode('utf-8'))








