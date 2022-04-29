import requests
import time
from datetime import date, timedelta
import re
import csv
import pandas as pd


def parse(data, other_info=[]):
    '''
    解析数据
    :param data:
    :param other_info:
    :return:
    '''
    if type(data) is str:
        data_list = data.split(',')
        # [开盘价，收盘价，最高价，最低价]
        return [data_list[1], data_list[2], data_list[3], data_list[4]]
    else:
        all_info = []
        if type(data) is list:
            for item in data:
                date_time = item.split(',')[0]
                amount = item.split(',')[5]
                item_data = ['sz002594', date_time, amount] + other_info

                all_info.append(item_data)
            save_file(all_info)


def save_file(data):
    with open('./stock_data.csv', 'w', encoding='gbk', newline='') as f:
        csv_f = csv.writer(f)
        csv_f.writerow(['代码', '成交时间', '成交数量', '当日最高价', '当日最低价', '当日开盘价', '当日收盘价'])
        csv_f.writerows(data)
        print('saved file!!!! ')


def get_other_info(headers):
    params = {
        'fields1': 'f1,f2,f3,f4,f5,f6',
        'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61',
        'ut': '7eea3edcaed734bea9cbfc24409ed989',
        'klt': 101,
        'fqt': 1,
        'secid': 0.002594,
        'beg': 0,
        'end': 20500000,
        '_': int(time.time() * 1000)
    }
    url = 'http://push2his.eastmoney.com/api/qt/stock/kline/get'
    try:
        res = requests.get(url, params=params, headers=headers)
    except Exception as e:
        raise e

    if res.status_code == 200:
        yesterday = str(date.today() + timedelta(days=-1))
        cmp = re.compile(f'"{yesterday}.*?"')
        data = cmp.search(res.text).group()
        return parse(data)
    else:
        print('获取 other info 失败')


def time_and_amount(other_info, headers):
    params = {
        'fields1': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13',
        'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58',
        'ut': '7eea3edcaed734bea9cbfc24409ed989',
        'ndays': 5,
        'iscr': 0,
        'secid': 0.002594,
        '_': int(time.time() * 1000)
    }
    url = 'http://push2his.eastmoney.com/api/qt/stock/trends2/get'
    try:
        res = requests.get(url, params=params, headers=headers)
    except Exception as e:
        raise e
    if res.status_code == 200:
        yesterday = str(date.today() + timedelta(days=-1))
        info = re.findall(f'"({yesterday}.*?)"', res.text)
        return parse(info, other_info)
    else:
        print('获取 time and amount 失败')


def data_handle():
    '''
    数据处理
    :return:
    '''
    df = pd.read_csv('./stock_data.csv', encoding='gbk')
    # print(df)

    df['成交量增减值'] = [i for i in df['成交数量'] - df['成交数量'].shift(1)]
    print(df)

    pos_count = len(df[df['成交量增减值'] > 0])
    neg_count = len(df[df['成交量增减值'] < 0])
    print('正增长数量：', pos_count)
    print('负增长数量：', neg_count)

    df['成交量增幅>2%'] = [1 if i > 0.02 else 0 for i in (df['成交数量'] - df['成交数量'].shift(1)) / df['成交数量'].shift(1)]
    print(df)


def main():
    headers = {
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Referer': 'http://quote.eastmoney.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }

    other_info = get_other_info(headers)
    time_and_amount(other_info, headers)
    data_handle()


if __name__ == '__main__':
    print('程序开启...')
    print('获取昨天的股票数据...')
    main()
    print('程序结束！！！')