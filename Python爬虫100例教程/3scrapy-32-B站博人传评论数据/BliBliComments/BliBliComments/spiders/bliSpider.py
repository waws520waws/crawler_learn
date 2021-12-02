import scrapy
import json

from BliBliComments.items import BliblicommentsItem

class BlispiderSpider(scrapy.Spider):
    name = 'bliSpider'
    # allowed_domains = ['www.xxx.com']

    start_urls = ['https://api.bilibili.com/pgc/review/short/list?media_id=5978&ps=20&sort=0']

    bade_url = 'https://api.bilibili.com/pgc/review/short/list?media_id=5978&ps=20&sort=0&cursor={}'

    def parse(self, response):
        json_data = json.loads(response.text)
        print(response.url)
        print(response.request.headers)
        if json_data['code'] == 0:
            if len(json_data['data']['list']) > 0:
                for one in json_data['data']['list']:
                    item = BliblicommentsItem()
                    item['uname'] = one['author']['uname']
                    item['content'] = one['content']
                    item['mid'] = one['mid']
                    item['likes'] = one['stat']['likes']

                    yield item

            cursor = json_data['data']['next']
            yield scrapy.Request(self.bade_url.format(cursor), callback=self.parse)
    '''
    start_urls = ['https://api.bilibili.com/pgc/review/short/list?media_id=5978&ps=20&sort=0']

    urls = ['https://www.baidu.com','https://shakarasquare.com/','https://baike.baidu.com/','https://baike.baidu.com/calendar/',
            'https://zhidao.baidu.com/','https://wenku.baidu.com/','https://image.baidu.com/','https://b2b.baidu.com/'
            ,'https://map.baidu.com/','http://news.baidu.com/','http://news.baidu.com/guonei','http://news.baidu.com/guoji']

    def parse(self, response):
        for url in self.urls:
            # print('一次一次一次一次一次一次一次！！！')
            yield scrapy.Request(url, callback=self.parse)
    '''
