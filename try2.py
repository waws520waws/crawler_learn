import requests

req = requests.get('https://www.baidu.com')
print(req.text)