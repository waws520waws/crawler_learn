import requests
import re
class VIP(object):
    def __init__(self):
        self.api = "http://y.mt2t.com/lines?url="
        self.url = "http://v.youku.com/v_show/id_XNDA0MDg2NzU0OA==.html?spm=a2h03.8164468.2069780.5"

    def run(self):
        res = requests.get(self.api+self.url)
        html = res.text

        key = re.search(r'key:"(.*?)"',html).group(1)
        print(key)

if __name__ == '__main__':
    vip = VIP()
    vip.run()
