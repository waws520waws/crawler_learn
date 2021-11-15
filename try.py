import requests_html

list_url = 'https://www.freetechbooks.com/topics?page=1'

session = requests_html.HTMLSession()
res = session.get(list_url)
res.encoding='utf-8'
href = res.html.xpath("//p[@class='h1']/text()")
print(href)

import requests
from lxml import etree

res = requests.get(list_url).text
page = etree.HTML(res)
href = page.xpath("//p[@class='h1']/text()")
print(href)
