import requests
from lxml import etree

res = requests.get('https://xclusiveloaded.com/dragon-beatz-with-me-ft-berry-l/').text

html = etree.HTML(res)
aa = html.xpath('//strong[contains(text(), "DOWNLOAD MP3")]/../@href')
print(aa)
