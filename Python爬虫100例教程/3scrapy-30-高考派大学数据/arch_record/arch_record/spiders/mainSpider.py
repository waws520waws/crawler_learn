'''
需求：
技术：
网站分析：网站往下翻会有'查看更多'，点击后发现请求方式变成了 POST。
    scrapy 模式是GET请求的，如果我们需要修改成POST，那么需要重写Spider类的start_requests(self) 方法，并且不再调用start_urls里面的url了
'''
import scrapy
from scrapy import FormRequest


class MainspiderSpider(scrapy.Spider):
    name = 'mainSpider'
    # allowed_domains = ['www.jzda001.coom']
    # start_urls = ['https://www.jzda001.coom']
    url = ['https://admin.jzda001.com/api/core/002--newsList']

    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36"
        }

    def start_requests(self):
        for i in range(1, 3):
            form_data = {
                'type': '1',
                'limit': '17',
                'pageNo': str(i)
            }
            request = FormRequest(self.url, headers=self.headers, formdata=form_data, callback=self.parse)
            yield request  # 因为有循环，得到一个结果就返回一个结果，防止一次性返回带来巨大的内存消耗

    def parse(self, response):
        pass
