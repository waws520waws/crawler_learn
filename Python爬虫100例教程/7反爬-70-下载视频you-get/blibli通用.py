'''
【注意】此案例对 bilibili 视频，进行下载，通用
'''

import requests
import re

url = 'https://www.bilibili.com/video/BV1Eq4y1m7AM'

url_headers = {
    'referer': 'https://www.bilibili.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
}

page = requests.get(url, headers=url_headers).text
# with open('./bilibili.html', 'w') as f:
#     f.write(req.text)

# with open('./bilibili.html', 'r', encoding='utf-8') as f:
#     page = f.read()

# 拿到高清视频地址
cmp1 = re.compile('"id":64.*?"baseUrl":"(.*?)"', re.S)
baseUrl = cmp1.search(page).group(1)
print(baseUrl)

## range 的取值范围可以先请求一次 baseUrl，然后在响应头中找到
bandwidth = '1111111'
video_range = 'bytes=0-' + bandwidth

base_headers = {
    'accept': '*/*',
    'accept-encoding': 'identity',
    'accept-language': 'zh-CN,zh;q=0.9',
    'if-range': 'Fri, 31 Dec 2021 00:58:42 GMT',
    'origin': 'https://www.bilibili.com',
    'range': video_range,
    'referer': url,
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
req = requests.get(baseUrl, headers=base_headers)
with open('./video1.mp4', 'wb') as f:
    f.write(req.content)
