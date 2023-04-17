import requests
import json
# 方法1
url = 'http://httpbin.org/get?name=王璐斯&age=19'
head = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
}
request = requests.get(url, headers=head)
print(json.loads(request.text))
print("------------------")
# 方法二
url1 = 'http://httpbin.org/get?name=&age=19'
pa = {
    'name':  '泮泮',
    'class': '19'
}
res = requests.get(url1, params=pa, headers=head)
print(json.loads(res.text))
import requests
import json
header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
"Cookie":'BIDUPSID=495EA7E4016DE7A0F1A198599D6EE632; PSTM=1642432121; BAIDUID=495EA7E4016DE7A056E7F9334F345F5C:FG=1; __yjs_duid=1_4f224fa438e1a40865095ee803595c5a1642432154106; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; SOUND_PREFER_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID_BFESS=495EA7E4016DE7A056E7F9334F345F5C:FG=1; BA_HECTOR=a10h0g24al2kak8g0k20a2ka1hj7c451b; ZFY=6q6grPtgS9PNQOPrXhBk2l6YMZnNpExViDs3j62cDKs:C; BDRCVFR[5ig7pqb-tu6]=mk3SLVN4HKm; H_PS_PSSID=; delPer=0; PSINO=2; BCLID=10831033599817018726; BCLID_BFESS=10831033599817018726; BDSFRCVID=6IuOJexroG0uo4Jj-zpIjclRpuweG7bTDYrEO43-ZR6EIc_VJeC6EG0Pts1-dEu-EHtdogKKBeOTHn0F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=6IuOJexroG0uo4Jj-zpIjclRpuweG7bTDYrEO43-ZR6EIc_VJeC6EG0Pts1-dEu-EHtdogKKBeOTHn0F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR3h3RrX26rDHJTg5DTjhPrMj4rtWMT-MTryKKJaaKbkj66uKMr8-PAwKhofKx-fKHnRh4oNBK-5Kfc-jxoz-p4ZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPULxo9LUvXtgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLK-oj-D8ljj023e; H_BDCLCKID_SF_BFESS=tR3h3RrX26rDHJTg5DTjhPrMj4rtWMT-MTryKKJaaKbkj66uKMr8-PAwKhofKx-fKHnRh4oNBK-5Kfc-jxoz-p4ZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPULxo9LUvXtgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLK-oj-D8ljj023e; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1662619524,1662619717,1664241699,1664333556; ab_sr=1.0.1_YTFkMTUxYmQ4MmM1MjM1NDFiYzUwOGQyOWMwMWNhZjU1Mzk1ODNhZmVhMDNjMmE0ZDQyMzU4NGIyZGUzNDA4MmFiNzk1ZjUzMTZiN2U4ZTE2N2RkZTA3YzkxODVmOWQwODQ2ZmFlZGVhMGEwMjZiMjBlMzI5YWVjMDVmNzljOTAzOWZlZTI3YWVmMmY5OWE5YjE0YzUxMzc5NjliZjBhZg==; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1664333565'
}
url1 = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
data1 = {
"from": "en",
"to": "zh",
"query": "aa",
"simple_means_flag": 3,
"sign": "922561.717040",
"token": "6510e2efe5f35c20c09eae8778ab18ce",
"domain": "common"
}
res1 = requests.post(url=url1, headers=header, data=data1)
w = (res1.text)
print(json.loads(w))



