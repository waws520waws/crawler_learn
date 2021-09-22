# 学习链接：https://www.bilibili.com/video/BV1Yh411o7Sz?p=36&spm_id_from=pageDriver
# https://book.apeland.cn/details/154/


import requests
import json

if __name__ == '__main__':
    url = 'https://movie.douban.com/typerank'
    param = {
        'type': '5',
        'interval_id': '100:90',
        'action': '',
        'start': '1',
        'limit': '20',
    }
    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.114 Safari/537.36'
    }

    req = requests.get(url, params=param, headers=header)

    list_page = req.json().decode('utf-8')

    fp = open(list_page, 'w', 'utf-8')

    json.dump(list_page, fp=fp, ensure_ascii=False)