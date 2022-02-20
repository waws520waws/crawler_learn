import requests
from lxml import etree

url = 'https://m.gmw.cn/toutiao/2022-02/19/content_35529067.htm'

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; SM-G973N Build/PPR1.190810.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 JsSdk/2 NewsArticle/8.2.8 NetType/wifi (NewsLite 8.2.8) JsSdk/2 NewsArticle/8.2.8 NetType/wifi (NewsLite 8.2.8)',

}

req = requests.get(url, headers=headers)
print(req.text)