import requests
from lxml import etree

url = 'https://www.today.ng/sport/basketball'


# 解决办法
# 首先 pip install cloudscraper

import cfscrape
# 实例化一个create_scraper对象
# scraper = cfscrape.create_scraper()
# 请求报错，可以加上时延
scraper = cfscrape.create_scraper(delay = 10)
# 获取网页源代码
req = scraper.post("http://example.com").text
print(req)


# req = requests.get(url)
print(req.status_code)
page = etree.HTML(req)
tab_p = page.xpath('//h2/a/text()')

print(tab_p)