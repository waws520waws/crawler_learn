import requests
from lxml import etree

req = requests.get('http://news.baidu.com/').text

page = etree.HTML(req)
info = page.xpath(r'//*[re:match(text(), ".*?总书记.*?")]', namespace={"re": "http://exslt.org/regular-expressions"})
print(info)
