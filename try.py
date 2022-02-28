import requests
from lxml import etree

with open('tt1.html', 'r', encoding='utf-8') as f:
    req = f.read()

page = etree.HTML(req)
cnt_div = page.xpath('//div[contains(@class, "entry-content")]/child::*')
print(cnt_div)
print('==================')
for div in cnt_div:
    print(div.tag)


dust_p = page.xpath('//div[contains(@class, "entry-content")]/p')
print(dust_p)
print('==================')
for i in cnt_div:
    if i in dust_p:
        print(i)
'''
<Element p at 0x7fb720474e10>, <Element p at 0x7fb720474e60>
'''