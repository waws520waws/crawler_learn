

# -*- coding: UTF-8 -*-
import requests  # 网络请求模块
import random  # 随机模块
import re  # 正则表达式模块
import time  # 时间模块
import threading  # 线程模块
import pymongo as pm   #mongodb模块
from lxml import etree

'''
参考：https://blog.csdn.net/hihell/article/details/82703695
需求：爬取图片网站的所有图片
技术：
'''


class Producer(threading.Thread):
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
        }

    def run(self):
        req = requests.get(self.url, headers=self.headers).text
        page = etree.HTML(req)
        detail_list = page.xpath('//p[@class="author-info-title"]/a/@href')






if __name__ == "__main__":
    # 起始种子地址
    url = ["https://douge2013.zcool.com.cn/follow?condition=0&p=1"]
    p = Producer(url)
