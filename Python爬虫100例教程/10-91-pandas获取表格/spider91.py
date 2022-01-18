
'''
使用 pandas 获取网页中的表格
'''

import pandas as pd
import requests

url = 'http://tjj.sjz.gov.cn/col/1584345166496/2020/09/07/1599460807453.html'

# read_html读取网页表格到 `list` of `DataFrame` （只能获取表格）
# 不能读取 https
# tb = pd.read_html(url)[3]  # 可直接读url，但不能防止反爬，下面是配合 requests 使用

r = requests.get(url)
r.encoding = "gb2312"
try:
    tb = pd.read_html(r.text, header=0)[0]  # header：指定哪一行作为header
    # 直接存储
    tb.to_csv('school.csv')
except Exception as e:
    print(e)