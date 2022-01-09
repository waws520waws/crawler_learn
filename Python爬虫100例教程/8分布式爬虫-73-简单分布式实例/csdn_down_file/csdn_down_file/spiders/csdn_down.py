import scrapy
from csdn_down_file.items import CsdnDownFileItem
import json
from scrapy_redis.spiders import RedisCrawlSpider


class CsdnDownSpider(RedisCrawlSpider):
    name = 'csdn_down'
    # allowed_domains = ['www.baidu.com']
    # start_urls = ['https://download.csdn.net/home/get_more_latest_source?page=1']

    print('1111111111111++++++++')

    redis_key = 'csdn:urls'

    def parse(self, response):
        print('parse++++++++++++++++++++++')
        item = CsdnDownFileItem()
        item['title'] = 'qqqq'

        yield item
        # print('asdadadadadsadaddadasds')
        # rs =  json.loads(response.text)
        # print(response.meta.get('page'))
        # page = 2
        # if response.meta.get('page') is not None:
        #     page = int(response.meta.get('page'))
        #     page += 1
        # if rs.get('message') == 'ok':
        #     # 取出数据
        #     data = rs.get('data').get('list')
        #     # 存取数据
        #     for content in data:
        #         file_id = content.get('id')
        #         title = content.get('title')
        #         source_url = content.get('download_source_url')
        #         item = CsdnDownFileItem(
        #             file_id=file_id,
        #             title=title,
        #             source_url=source_url
        #         )
        #         print(file_id)
        #         yield item
        #
        # next_url = f"https://download.csdn.net/home/get_more_latest_source?page={page}"
        # yield scrapy.Request(url=next_url, callback = self.parse, meta = {'page': page})

