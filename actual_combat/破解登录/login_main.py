'''
网站：https://bqcm0.cavip1.com/
破解登录的加密参数
'''

import execjs

username = "q778899"
password = "123456"

with open('./code.js', 'r', encoding='utf-8') as f:
    jscode = f.read()

docjs = execjs.compile(jscode)
params = docjs.call('getparam', username, password)

print(params)