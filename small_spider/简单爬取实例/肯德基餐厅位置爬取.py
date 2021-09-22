import requests

if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/storelist/index.aspx'

    param = {
        'cname': '',
        'pid': '',
        'keyword': '成都',
        'pageIndex': '1',
        'pageSize': '10'
    }

    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.114 Safari/537.36'
    }
    req = requests.post(url, params=param, headers=header)

    data = req.text

    print(data)

