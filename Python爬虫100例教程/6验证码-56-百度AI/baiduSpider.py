
'''
此案例是调用百度的api来识别验证码
步骤：
    1、百度平台 -》'应用列表' -〉创建应用 -》得到API key、secret key
    2、请求得到 access_token
    3、图片编码
    4、最后请求某功能api的url，得到结果
'''

import json
import base64
import requests


class VerificationCode():
    def __init__(self):
        self.token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={0}&client_secret={1}'
        self.api_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token={}"
        self.API = 'AVrds9vALBzv0VQ7xu8Z6A6f'
        self.secret = 'WzQZXcDEABGoMc3afGwqEbWjqX4QnuQL'

    def get_accesstoken(self):
        res = requests.post(self.token_url.format(self.API, self.secret))
        content = res.text
        if content:
            return json.loads(content)["access_token"]

    def show_code(self):
        # 二进制方式打开图片文件
        with open('./3.png', 'rb') as f:
            img = base64.b64encode(f.read())

        params = {"image": img}
        access_token = self.get_accesstoken()
        request_url = self.api_url.format(access_token)
        headers = {
            'content-type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json())


if __name__ == '__main__':
    v = VerificationCode()
    v.show_code()

