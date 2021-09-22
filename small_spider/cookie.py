# 学习链接：https://www.bilibili.com/video/BV1Yh411o7Sz?p=36&spm_id_from=pageDriver
# https://book.apeland.cn/details/154/

'''
- cookie: 用来让服务器记录客户端的相关状态（如登录状态）
- 如何获取cookie值：
    - 使用session会话对象：
        - session的作用：
            1、可以进行请求
            2、如果请求过程中产生了cookie，则该cookie会被自动存储或携带在该session对象中

- token：Token是服务端生成的一串字符串，以作客户端进行请求的一个令牌，当第一次登录后，服务器生成一个Token便将此Token返回给客户端，
以后客户端只需带上这个Token前来请求数据即可，无需再次带上用户名和密码。
- 如何获取token值：
    - token值一般都会动态存在与该请求对应的前台页面中（前段网页源码中）
'''

import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/72.0.3626.121 Safari/537.36'
}

session = requests.session()


# 获取动态token值（因为后边请求页面的参数里有token，所以要先获取token）

page_text = session.get(url='https://github.com/login', headers=headers).text

login_page = etree.HTML(page_text)

token = login_page.xpath('//input[@name="authenticity_token"]/@value')[0]


# 模拟登录，请求页面

params = {
    'commit': 'Sign in',
    'authenticity_token': token,
    'login': 'Jie-Ge',
    'password': 'jie970706',
    'trusted_device': '',
    'webauthn-support': 'supported'
}
# 使用会话对象进行模拟登录请求发送（携带cookie）
page_text = session.post(url='https://github.com/session', headers=headers, params=params).text

with open('./github.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)