# 学习链接：https://www.bilibili.com/video/BV1Yh411o7Sz?p=36&spm_id_from=pageDriver
# https://book.apeland.cn/details/154/

import requests
import json

'''
列表页、详情页都是ajax动态加载的数据
'''


if __name__ == '__main__':

    # 获取列表页数据

    ### ajax请求数据的url
    list_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'

    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.114 Safari/537.36'
    }

    param1 = {
        'page': '1',
        'pageSize': '15',
        'conditionType': '1'
    }

    req = requests.post(list_url, params=param1, headers=header)

    ### dic格式数据
    json_data = req.json()

    # 获取详情页数据

    ### ajax请求数据的url
    detail_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for dic in json_data['list']:
        id = dic['ID']
        param2 = {
            'id': id
        }
        detail_data = requests.post(detail_url, params=param2, headers=header).json()
        print(detail_data)
        break
