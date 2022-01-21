import requests
res = requests.get('https://www.baidu.com')
text = res.text
print('this is my first to use server, success!!!')