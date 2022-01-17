import pandas as pd
import requests
url = 'http://www.hbdzxx.com/news/2015/1.html'
r = requests.get(url)
r.encoding = "gb2312"
try:
    tb = pd.read_html(r.text,header=0)[0]
    # 直接存储
    tb.to_csv('school.csv')
except Exception as e:
    print(e)
