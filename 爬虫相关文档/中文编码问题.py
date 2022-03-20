import requests

url = ''

# 中文乱码问题

## 1、可以在请求时设置编码（也可能是gbk格式）
req = requests.get(url).encoding('utf-8')
html = req.text

## 2、可以将乱码数据先编码，再解码
data = '乱码'
# iso-8859-1：是单字节编码，向下兼容ASCII
data = data.encode('iso-8859-1').decode('gbk')