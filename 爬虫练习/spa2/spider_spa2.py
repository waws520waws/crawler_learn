'''
爬虫练习网站：https://cuiqingcai.com/9522.html

此案例解决 token 加密
'''

# 解决 execjs模块报错的问题（这三句话，在导入 execjs之前写进去）
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

import requests
import execjs
with open('token.js', 'r', encoding='utf-8') as f:
    jscode = f.read()

docjs = execjs.compile(jscode)
token = docjs.call('get_token')
print(token)

url = 'https://spa2.scrape.center/api/movie/'

params = {
    'limit': 10,
    'offset': 0,
    'token': token
}

res = requests.get(url, params=params, timeout=5)
print(res.text)