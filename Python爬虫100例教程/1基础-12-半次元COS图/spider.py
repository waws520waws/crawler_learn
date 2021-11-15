from datetime import date, datetime, timedelta
import pymongo
import requests
import random

'''
url：https://bcy.net/illust/toppost100
网页特点：瀑布流，下滑到网页底部时动态加载数据
动态数据请求url：https://bcy.net/apiv3/rank/list/itemInfo?p=2&ttype=illust&sub_type=week&date=20211112

'''

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
eg_100_db = myclient['eg_100_db']
index = 0


def get_request(date_date):

    url = 'https://bcy.net/apiv3/rank/list/itemInfo'
    page_num = 0
    date_str = date_date.strftime('%Y%m%d')
    while True:
        page_num += 1
        params = {
            'p': page_num,
            'ttype': 'illust',
            'sub_type': 'week',
            'date': date_str
        }

        user_agent = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36"
        ]
        headers = {'user-agent': random.choice(user_agent)}

        try:
            req = requests.get(url, params=params, headers=headers)
            req_data = req.json()
            pic_data = []
            global index
            if req_data['data']['top_list_item_info']:
                for item in req_data['data']['top_list_item_info']:
                    pic_data.append({'index': index,
                                     'uname': item['item_detail']['uname'],
                                     'uid': item['item_detail']['uid'],
                                     'pic': item['item_detail']['cover']})
                    index += 1

                # 存储数据
                eg_100_db.pic_12.insert_many(pic_data)

            else:
                print(f'{date_str} 日期下的数据已采集完')
                break

        except Exception as e:
            print('yichang!!!!', e)


def main():
    date_date = date.today()
    day = 2  # 取3天的
    while day > 0:
        print('正在下载 %s 的数据 >>>>>>>>>' % date_date)
        get_request(date_date)
        date_date = date.today() + timedelta(days=-1)
        day -= 1


if __name__ == '__main__':
    main()